from mapmanager.zabbix_api.config import *
import math

def create_elements(hosts_elements, qt_elements):
    # Define o tamanho do mapa
    map_width = 80 * qt_elements
    map_height = map_width
    
    max_hosts = 600

    if qt_elements > max_hosts:
        mensagem = f"Parando a execução do script porque o número de hosts para adicionar ao mapa '{qt_elements}' excede o máximo permitido.\n-> Máximo permitido: '{max_hosts} hosts'"
        exit()

    num_columns = int(math.sqrt(qt_elements))
    num_rows = math.ceil(qt_elements / num_columns)

    x_spacing = map_width // num_columns
    y_spacing = map_height // num_rows

    elements = []
    hosts_dict = {host['host']: host for host in hosts_elements}
    hosts_elements = list(hosts_dict.values())

    for index, host in enumerate(hosts_elements):
        x = (index % num_columns) * x_spacing + x_spacing // 2
        y = (index // num_columns) * y_spacing + y_spacing // 2

        host_type = next((key for key in ICON_MAP if key in host['host']), None)
        
        icon_ids = ICON_MAP[host_type] if host_type else DEFAULT_ICONS

        element = {
            "selementid": str(len(elements) + 1),
            "elements": [{"hostid": host['hostid']}],
            "elementtype": 0,
            "label": "{HOST.HOST}\r\n{HOST.IP}\r\n{INVENTORY.MODEL}",
            "x": x,
            "y": y,
            "iconid_off": icon_ids[0],
            "iconid_on": icon_ids[1],
            "iconid_disabled": icon_ids[2],
            "iconid_maintenance": icon_ids[3]
        }

        elements.append(element)
    
    mensagem = "Elementos criados"

    return elements, map_width, map_height, mensagem
