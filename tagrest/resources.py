from flask_restful import Resource
from tagrest.db import get_db


class Hash(Resource):
    def get(self, globaltag, kind, runnumber):
        hash = get_db().execute(
                "SELECT hash"
                f" FROM {kind} p JOIN global_tag_map u ON p.tag = u.{kind}"
                f" WHERE u.global_tag = {globaltag} AND p.run_number = {runnumber}"
            ).fetchone()
        return hash[0]


class Payload(Resource):
    def get(self, hash):
        payload = get_db().execute(
                "SELECT payload"
                f" FROM payload p WHERE p.hash = '{hash}'"
            ).fetchone()
        return payload[0]
        #return bytes.fromhex(payload[0]).decode('utf-8')


class TagMap(Resource):
    def get(self, globaltag):
        row = get_db().execute(
                "SELECT *"
                f" FROM global_tag_map"
                f" WHERE global_tag_map.global_tag = {globaltag}"
            ).fetchone()
        kind_tag_dict = dict(zip(row.keys(), tuple(row)))
        tag_map = {}
        for kind, tag in kind_tag_dict.items():
            if kind == 'id' or kind =='global_tag':
                continue
            tag_map[kind] = []
            sub_row = get_db().execute(
                "SELECT *"
                f" FROM {kind}"
                f" WHERE {kind}.tag = {tag}"
            ).fetchall()
            for sr in sub_row:
                t = tuple(sr)
                tag_map[kind].append({t[1]: t[2]})
        return tag_map


class FastTagMap(Resource):
    def get(self, globaltag):
        res = get_db().execute(
            "SELECT h.kind, run_number, hash"
            f" FROM global_tag_map_new g JOIN hash_map h ON g.tag=h.tag"
            f" WHERE g.global_tag = {globaltag}"
        )
        tag_map = {}
        for row in res:
            t = tuple(row)
            try:
                tag_map[t[0]].append({t[1]:t[2]})
            except KeyError:
                tag_map[t[0]] = [{t[1]: t[2]}]
        return tag_map