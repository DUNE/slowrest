import sqlite3
import cx_Oracle
import os

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext
import sys


if sys.platform.startswith("darwin"):
    lib_dir = os.path.join(os.environ.get("HOME"), "Downloads", "instantclient_19_8")
elif sys.platform.startswith("win32"):
    lib_dir = r"C:\oracle\instantclient_19_9"
cx_Oracle.init_oracle_client(lib_dir=lib_dir)


@classmethod
def setup_from_config(cls, cfg_file='conf/backend/db_pool.json'):
    with open(cfg_file) as f:
        cfg = json.load(f)
    cls.db_pool = cx_Oracle.SessionPool(cfg['user'], cfg['pass'], cfg['dsn'], cfg['min'], cfg['max'], cfg['increment'],
                                        threaded=True)


@classmethod
def _prepare_cursor(cls, query, bind_variables):
    connection = cls.db_pool.acquire()
    cursor = connection.cursor()
    cursor.execute(query, bind_variables)
    return cursor


@classmethod
def perform_query(cls, query, bind_variables, resultset):
    """query the db and store result in *resultset*"""
    cursor = cls._prepare_cursor(query, bind_variables)
    while True:
        qres = cursor.fetchmany()
        if not len(qres) == 0:
            resultset.append(qres)
        if not qres:
            break;


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
#        g.db = sqlite3.connect(
#            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
#        )
#        g.db.row_factory = sqlite3.Row
#        db_pool = cx_Oracle.SessionPool(current_app.config["DATABASE"])
        db_pool = cx_Oracle.SessionPool(user='user', password='pwd', dsn='localhost')
        g.db = cx_Oracle.connect(
            current_app.config["DATABASE"], detect_types=cx_Oracle.PARSE_DECLTYPES
        )
        g.db.row_factory = cx_Oracle.Row
    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()
    with current_app.open_resource("sql/schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


def fill_db():
    """Populate DB with example data"""
    db = get_db()
    with open(os.path.join(os.path.dirname(__file__), "../tests/data.sql"), "rb") as f:
        db.executescript(f.read().decode("utf8"))


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


@click.command("fill-db")
@with_appcontext
def fill_db_command():
    fill_db()
    click.echo("Populated the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(fill_db_command)