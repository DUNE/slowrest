import oracledb
import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext
from slowrest.config import conn


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        c = oracledb.connect(
            user=conn.un, password=conn.pw, dsn=conn.cs
        )
        g.db = c.cursor()
    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)
    if db is not None:
        db.close()


def test_print():
    print(f'This is the test print')


@click.command("test-command")
@with_appcontext
def test_print_command():
    test_print()
    click.echo("Conducted test command.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(test_print_command)
