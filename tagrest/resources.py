from flask_restful import Resource
from flask import request
from tagrest.db import get_db
from tagrest.sql import queries
from tagrest.utils import extract_tag_map_from_results
from tagrest import cache


class Index(Resource):
    @staticmethod
    def get():
        return "Welcome to tagrest!"


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


class TagMap(Resource):
    @staticmethod
    def get(globaltag):
        kind_tag_dict = GlobalTag.get(globaltag)
        res = get_db().execute(
            queries.Get.tag_map(kind_tag_dict)
        )
        return extract_tag_map_from_results(res)


class GlobalTag(Resource):
    @staticmethod
    @cache.cached(timeout=300)
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




################## EXPERIMENTAL ##################

class FastTagMap(Resource):
    def get(self, globaltag):
        res = get_db().execute(
            queries.Get.fast_tag_map(globaltag)
        )
        return extract_tag_map_from_results(res)


class Test(Resource):
    def get(self):
        res = get_db().execute(
            queries.test()
        )
        for row in res:
            print(tuple(row))
        return 1
