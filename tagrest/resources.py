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
