from flask_restful import Resource
from slowrest.db import get_db
from slowrest import queries
from slowrest import cache
from datetime import datetime, timezone, timedelta


def get_value_pair_dict(from_ts, to_ts, sensor_id) -> dict:
    query = get_db().execute(
        queries.value_pairs_time_range,
        sensor_id=sensor_id, from_ts=from_ts, to_ts=to_ts
    )
    value_pair_dict = {}
    for vp in query.fetchall():
        dt = vp[0].replace(tzinfo=timezone.utc)
        ts = round(dt.timestamp()*1000) # rounded to millisecond
        value_pair_dict[ts] = vp[1]
    return value_pair_dict


class Index(Resource):
    @staticmethod
    def get():
        return "Welcome to slowrest!"


class Day(Resource):
    """returns {'ts_1': value_1, 'ts_2': value_2, ...}"""
    @staticmethod
    @cache.cached()
    def get(day, sensor_id) -> dict:
        from_ts = datetime.fromisoformat(day).replace(tzinfo=timezone.utc)
        to_ts = from_ts + timedelta(days=1)
        return get_value_pair_dict(from_ts, to_ts, sensor_id)


class Range(Resource):
    """returns {'ts_1': value_1, 'ts_2': value_2, ...}"""
    @staticmethod
    @cache.cached()
    def get(begin, end, sensor_id) -> dict:
        from_ts = datetime.fromisoformat(begin).replace(tzinfo=timezone.utc)
        to_ts = datetime.fromisoformat(end).replace(tzinfo=timezone.utc)
        return get_value_pair_dict(from_ts, to_ts, sensor_id)


class SensorDict(Resource):
    """returns {'id_1': 'name_1', 'id_2': 'name_2', ...}"""
    @staticmethod
    @cache.cached()
    def get() -> dict:
        query = get_db().execute(
            queries.sensor_id_name_pairs,
        )
        return dict(query.fetchall())


class SensorName(Resource):
    @staticmethod
    def get(sensor_id) -> str:
        return SensorDict.get()[sensor_id]
