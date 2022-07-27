from flask_restful import Resource
from tagrest.db import get_db
from tagrest.sql import queries


class Hash(Resource):
    def get(self, globaltag, kind, runnumber):
        hash = get_db().execute(
            queries.hash(globaltag, kind, runnumber)
        ).fetchone()
        return hash[0]


class Payload(Resource):
    def get(self, hash):
        payload = get_db().execute(
            queries.payload(hash)
        ).fetchone()
        return payload[0]


class TagMap(Resource):
    def get(self, globaltag):
        kind_tag_dict = GlobalTag.get(globaltag)
        res = get_db().execute(
            queries.tag_map(kind_tag_dict)
        )
        return extract_tag_map_from_results(res)


class FastTagMap(Resource):
    def get(self, globaltag):
        res = get_db().execute(
            queries.fast_tag_map(globaltag)
        )
        return extract_tag_map_from_results(res)


class GlobalTag(Resource):
    @staticmethod
    def get(globaltag):
        row = get_db().execute(
            queries.global_tag(globaltag)
        ).fetchone()
        kind_tag_dict = dict(zip(row.keys()[1:], tuple(row[1:])))
        return kind_tag_dict


def extract_tag_map_from_results(res):
    tag_map = {}
    for row in res:
        t = tuple(row)
        try:
            tag_map[t[0]].append({t[1]: t[2]})
        except KeyError:
            tag_map[t[0]] = [{t[1]: t[2]}]
    return tag_map
