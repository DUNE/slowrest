from flask_restful import Resource
from flask import request
from slowrest.db import get_db
from slowrest.sql import queries
from slowrest.utils import extract_tag_map_from_results
from slowrest import cache


class Index(Resource):
    @staticmethod
    def get():
        return "Welcome to slowrest!"


class Day(Resource):
    @staticmethod
    def get(day, elId):
        return 'yo'


class Hash(Resource):
    @staticmethod
    def get(kind, tag, runnumber):
        hash = get_db().execute(
            queries.Get.hash(tag, kind, runnumber)
        ).fetchone()
        return hash[0]

    @staticmethod
    def post(kind, tag, runnumber):
        hash = request.get_data().decode("utf-8")
        get_db().executescript(
            queries.Post.hash(tag, kind, runnumber, hash)
        )


class Payload(Resource):
    @staticmethod
    def get(hash):
        payload = get_db().execute(
            queries.Get.payload(hash)
        ).fetchone()
        return payload[0]

    @staticmethod
    def post(hash):
        payload = request.get_json()
        get_db().executescript(
            queries.Post.payload(hash, payload)
        )



class TagMap(Resource):
    @staticmethod
    @cache.cached()
    def get(globaltag):
        kind_tag_dict = GlobalTag.get(globaltag)
        res = get_db().execute(
            queries.Get.tag_map(kind_tag_dict)
        )
        return extract_tag_map_from_results(res)


class GlobalTag(Resource):
    @staticmethod
    @cache.cached()
    def get(globaltag):
        row = get_db().execute(
            queries.Get.global_tag(globaltag)
        ).fetchone()
        kind_tag_dict = dict(zip(row.keys()[1:], tuple(row[1:])))
        return kind_tag_dict

    @staticmethod
    def post(globaltag):
        data = request.get_json()
        get_db().executescript(
            queries.Post.global_tag(globaltag, data)
        )
