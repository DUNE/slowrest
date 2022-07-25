from flask_restful import Resource
from tagrest.db import get_db


class Hash(Resource):
    def get(self, globaltag, kind, runnumber):
        hash = get_db().execute(
                "SELECT hash"
                " FROM sce p JOIN global_tag_map u ON p.tag = u.sce"
                " WHERE u.global_tag = '2.0'"
            ).fetchone()
        for key in hash.keys():
            print(f'key = {key}')
        for row in hash:
            print(f'row = {row}')
        return "HASH"


#        hash = get_db().execute(
#                "SELECT p.id, title, body, created, author_id, username"
#                " FROM post p JOIN user u ON p.author_id = u.id"
#                " WHERE p.id = ?",
#                (id,),
#            ).fetchone()
