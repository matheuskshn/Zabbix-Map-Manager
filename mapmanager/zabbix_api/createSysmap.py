from mapmanager.zabbix_api.config import *

def create_sysmap(map_name, map_width=500, map_height=500):
    map_params = {
        "name": map_name,
        "userid": USERID,
        "width": map_width,
        "height": map_height,
        "backgroundid": BACKGROUNDID,
        "expandproblem": EXPANDPROBLEM,
        "expand_macros": EXPANDMACROS,
        "markelements": MARKELEMENTS,
        "show_suppressed": SHOW_SUPPRESSED,
        "severity_min": SEVERITY_MIN,
        "highlight": HIGHLIGHT,
        "label_type": LABEL_TYPE,
        "private": PRIVATE,
    }

    return map_params