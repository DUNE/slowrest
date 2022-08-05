from flask_restful import Resource
from flask import request
from slowrest.db import get_db
from slowrest import queries
#from slowrest.utils import extract_tag_map_from_results
from slowrest import cache
#from datetime import datetime
import datetime


class Index(Resource):
    @staticmethod
    def get():
        return "Welcome to slowrest!"


class Day(Resource):
    @staticmethod
    def get(day, sensor_id):
        from_ts = datetime.date(2019, 4, 20)
#        from_ts = datetime.datetime(2019, 4, 20, 23, 59, 0)
        to_ts = datetime.date(2019, 4, 21)
        print(f'from_ts = {from_ts}')
        print(f'to_ts = {to_ts}')
        t_0 = datetime.datetime.now()
        res = get_db().execute(
            queries.value_pairs_time_range2,
            sensor_id=sensor_id, from_ts=from_ts, to_ts=to_ts
        )
        arr = res.fetchall()
        print(f'took {datetime.datetime.now() - t_0} sec')
#        for r in res:
#            print(f'r = {r}')
#        print(f'res.fetchall() = {arr}')
        return 'yo'


class SensorName(Resource):
    @staticmethod
    def get(sensor_id):
        res = get_db().execute(
            queries.sensor_name,
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
