from flask_restful import Resource
from slowrest.db import get_db
from slowrest import queries
from slowrest.cache import cache
from datetime import datetime, timezone, timedelta


def get_value_pair_dict(from_ts, to_ts, sensor_id) -> dict:
    query = get_db().execute(
        queries.value_pairs_time_range,
        sensor_id=sensor_id, from_ts=from_ts, to_ts=to_ts
    )
    value_pair_dict = {}
    for vp in query.fetchall():
        dt = vp[0].replace(tzinfo=timezone.utc)
        ts = round(dt.timestamp()*1000)  # rounded to millisecond
        value_pair_dict[ts] = vp[1]
    return value_pair_dict

def add_dynamic_resource(api, resource_name, sensor_list, url_path):
    """Factory method that creates dynamic resources
       based on the files in sensor_lists folder."""

    def init(self): 
        self.sensor_list = sensor_list 

    def get_entries(self) -> dict:
        sensor_list = ",".join([str(i) for i in self.sensor_list])
        query = get_db().execute(
        queries.sensors_current_value.format(sensor_list)
        )
        
        response_dict = {}
        for sens_id, value, ts in query.fetchall():
            response_dict[sens_id] = (value, ts.isoformat())
             
        return response_dict

    dynamic_resource = type(resource_name,
                            (Resource,),
                            {"__init__": init,
                             'get': get_entries})

    api.add_resource(dynamic_resource, url_path)


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
            queries.sensor_id_name_pairs
        )
        return dict(query.fetchall())


class SensorName(Resource):
    @staticmethod
    def get(sensor_id) -> str:
        return SensorDict.get()[sensor_id]
