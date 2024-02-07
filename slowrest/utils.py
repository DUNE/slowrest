import os
from functools import lru_cache

PATH_PREFIX = f"{os.path.dirname(__file__)}/sensor_lists"


@lru_cache(maxsize=2)
def get_page_sensor_dict() -> dict:
    filename_list = os.listdir(PATH_PREFIX)

    id_lists_dict = {}
    for fn in filename_list:
        with open(f"{PATH_PREFIX}/{fn}", "r") as f:
            data = f.readlines()
            data = filter(None, map(str.strip, data))
            data = list(map(int, data))
        id_lists_dict[fn] = data

    return id_lists_dict
