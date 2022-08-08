from flask_restful import Resource
from flask import request
from slowrest.db import get_db
from slowrest import queries
from slowrest import cache
import datetime


class Index(Resource):
    @staticmethod
    def get():
        return "Welcome to slowrest!"


class Day(Resource):
    @staticmethod
    @cache.cached()
    def get(day, sensor_id):
        print("Day.get()")
        from_ts = datetime.datetime.strptime(day, '%Y-%m-%d')
        to_ts = from_ts + datetime.timedelta(days=1)
        res = get_db().execute(
            queries.value_pairs_time_range,
            sensor_id=sensor_id, from_ts=from_ts, to_ts=to_ts
        )
        return Day._get_timestamped_values(res)

    @staticmethod
    def _get_timestamped_values(query_result):
        new_vps = []
        for vp in query_result.fetchall():
            ts = int(datetime.datetime.timestamp(vp[0])*1000)
            new_vps.append([ts, vp[1]])
        return new_vps


class SensorDict(Resource):
    """{'id_1': 'name_1', 'id_2': 'name_2', ...}"""
    @staticmethod
    @cache.cached()
    def get() -> dict:
        print("SensorDict.get()")
        res = get_db().execute(
            queries.sensor_id_name_pairs,
        )
        return SensorDict._get_sensor_dict(res)

    @staticmethod
    def _get_sensor_dict(query_result):
        sensor_dict = {}
        for pair in query_result.fetchall():
            sensor_dict[pair[0]] = pair[1]
        return sensor_dict


class SensorName(Resource):
    @staticmethod
    def get(sensor_id) -> int:
        return SensorDict.get()[sensor_id]
