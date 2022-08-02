def extract_tag_map_from_results(res):
    tag_map = {}
    for row in res:
        t = tuple(row)
        try:
            tag_map[t[0]][t[1]] = t[2]
        except KeyError:
            tag_map[t[0]] = {t[1]: t[2]}
    return tag_map
