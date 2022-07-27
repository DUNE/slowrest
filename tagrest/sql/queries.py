def global_tag(gt):
    return f"SELECT *"\
           f" FROM global_tag_map"\
           f" WHERE global_tag_map.global_tag = {gt}"


def hash(gt, kind, rn):
    return f"SELECT hash"\
           f" FROM {kind} p JOIN global_tag_map u ON p.tag = u.{kind}"\
           f" WHERE u.global_tag = {gt} AND p.run_number = {rn}"


def payload(hash):
    return f"SELECT payload"\
           f" FROM payload p WHERE p.hash = '{hash}'"


def fast_tag_map(gt):
    return f"SELECT h.kind, run_number, hash"\
           f" FROM global_tag_map_new g JOIN hash_map h ON g.tag=h.tag"\
           f" WHERE g.global_tag = {gt}"


def tag_map(kind_tag_dict):
    first = True
    for kind, tag in kind_tag_dict.items():
        if first:
            qs = f"SELECT '{kind}' as 'kind', run_number, hash\n"
            first = False
        else:
            qs += f" UNION SELECT '{kind}' as 'kind', run_number, hash\n"
        qs += f" FROM {kind} WHERE {kind}.tag = {tag}\n"
    print(f'qs =\n{qs}')
    return qs
