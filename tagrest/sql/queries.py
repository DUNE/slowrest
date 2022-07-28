class Get:
    @staticmethod
    def global_tag(gt):
        return f"SELECT *"\
               f" FROM global_tag_map"\
               f" WHERE global_tag_map.global_tag = {gt}"

    @staticmethod
    def hash(tag, kind, rn):
        return f"SELECT hash FROM {kind} k"\
               f" WHERE k.tag = {tag} AND k.run_number = {rn}"

    @staticmethod
    def payload(hash):
        return f"SELECT payload"\
               f" FROM payload p WHERE p.hash = '{hash}'"

    @staticmethod
    def fast_tag_map(gt):
        return f"SELECT h.kind, run_number, hash"\
               f" FROM global_tag_map_new g JOIN hash_map h ON g.tag=h.tag"\
               f" WHERE g.global_tag = {gt}"

    @staticmethod
    def tag_map(kind_tag_dict):
        first = True
        for kind, tag in kind_tag_dict.items():
            if first:
                qs = f"SELECT '{kind}' as 'kind', run_number, hash\n"
                first = False
            else:
                qs += f" UNION SELECT '{kind}' as 'kind', run_number, hash\n"
            qs += f" FROM {kind} WHERE {kind}.tag = {tag}\n"
        return qs


class Post:
    @staticmethod
    def global_tag(gt, kind_tag_dict):
        ins_str = "global_tag"
        val_str = gt
        for kind, tag in kind_tag_dict.items():
            ins_str += f", {kind}"
            val_str += f", {tag}"
        qs = f"INSERT INTO global_tag_map ({ins_str})\n" \
             f"VALUES\n" \
             f" ({val_str})"
        return qs

    @staticmethod
    def hash(tag, kind, rn, hash):
        return f"INSERT INTO {kind} (tag, run_number, hash)" \
               f"VALUES" \
               f"  ({tag}, {rn}, {hash})"


################## EXPERIMENTAL ##################

def hash_old(gt, kind, rn):
    return f"SELECT hash"\
           f" FROM {kind} k JOIN global_tag_map g ON k.tag = g.{kind}"\
           f" WHERE g.global_tag = {gt} AND k.run_number = {rn}"

def test():
    return f"SELECT 'sce' as kind, run_number, hash FROM sce" \
           f" WHERE tag = (" \
           f" SELECT sce FROM global_tag_map" \
           f"  WHERE global_tag_map.global_tag = '2.0')" \
           f" UNION SELECT 'lifetime' as kind, run_number, hash FROM lifetime" \
           f"  WHERE tag = (" \
           f"  SELECT lifetime FROM global_tag_map" \
           f"   WHERE global_tag_map.global_tag = '2.0')"