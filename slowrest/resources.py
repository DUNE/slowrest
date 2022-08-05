from flask_restful import Resource
from flask import request
from slowrest.db import get_db
from slowrest import queries
from slowrest.utils import extract_tag_map_from_results
from slowrest import cache


class Index(Resource):
    @staticmethod
    def get():
        return "Welcome to slowrest!"


class Day(Resource):
    @staticmethod
    def get(day, sensor_id):
        res = get_db().execute(
            queries.get_value_pairs_for_day,
            day=day, sensor_id=sensor_id
        )
        for r in res:
            print(f'r = {r}')
        return 'yo'


class SensorName(Resource):
    @staticmethod
    def get(sensor_id):
        res = get_db().execute(
            queries.get_sensor_name,
            sensor_id=sensor_id
        )
        print(f'res = {res}')
        for r in res:
            print(f'r = {r}')
        return 'yo'


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
