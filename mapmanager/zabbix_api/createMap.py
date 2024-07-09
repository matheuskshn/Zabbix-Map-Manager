from mapmanager.zabbix_api.config import *
from mapmanager.zabbix_api.createSysmap import create_sysmap
from mapmanager.zabbix_api.getHosts import get_hosts
from mapmanager.zabbix_api.createElements import create_elements
from mapmanager.zabbix_api.getCdpItems import *
from mapmanager.zabbix_api.createLinks import create_links
from mapmanager.zabbix_api.zabbixApiAuth import authenticate

zbx_url = ZABBIX_URL if ZABBIX_URL else ''
zbx_api_url = ZABBIX_API_URL if ZABBIX_API_URL else ''
zbx_user = ZABBIX_USER if ZABBIX_USER else ''
zbx_pass = ZABBIX_PASSWORD if ZABBIX_PASSWORD else ''
zbx_api_token = ZABBIX_API_TOKEN if ZABBIX_API_TOKEN else ''

def main(map_name, map_groups, map_hosts, map_ips, map_hosts_filter, create_link, add_trigger, trigger_icmp, trigger_snmp):
    zapi = authenticate(zbx_api_url, zbx_user, zbx_pass, zbx_api_token)
    mensagem = ""
    new_map = None
    links = []

    if map_name:
        if map_groups or map_hosts or map_ips or map_hosts_filter:
            hosts_elements = get_hosts(zapi, map_groups, map_hosts, map_ips, map_hosts_filter)
            elements, map_width, map_height, mensagem = create_elements(hosts_elements[0], hosts_elements[6])
            map_params = create_sysmap(map_name, map_width, map_height)
            map_params['selements'] = elements

            if create_link:
                neighbors = get_neighbors(zapi, hosts_elements[0])
                links = create_links(elements, neighbors, zapi, trigger_icmp, trigger_snmp)
                map_params['links'] = links

            create_result = zapi.map.create(map_params)
            print(create_result)
            sysmapid = create_result['sysmapids'][0]
            new_map = map_params
            map_link = f"{zbx_url}zabbix.php?action=map.view&sysmapid={sysmapid}"
            new_map = map_params
        else:
            mensagem = 'Criando mapa sem elementos'
            map_params = create_sysmap(map_name)
            create_result = zapi.map.create(map_params)
            print(create_result)
            sysmapid = create_result['sysmapids'][0]
            new_map = map_params
            map_link = f"{zbx_url}zabbix.php?action=map.view&sysmapid={sysmapid}"
    else:
        mensagem = "Nome do mapa não fornecido"

    # Retorno para map_result.html:
    return {
        'sysmapid': sysmapid,
        'map_link': map_link,
        'map_name': map_name,
        'map_groups': map_groups,
        'map_hosts': map_hosts,
        'map_ips': map_ips,
        'map_hosts_filter': map_hosts_filter,
        'create_link': create_link,
        'add_trigger': add_trigger,
        'trigger_icmp': trigger_icmp,
        'trigger_snmp': trigger_snmp,
        'mensagem': mensagem,
        'host_elements': hosts_elements[0] if 'hosts_elements' in locals() else None,
        'qt_found_group': hosts_elements[1] if 'hosts_elements' in locals() else None,
        'qt_found_host': hosts_elements[2] if 'hosts_elements' in locals() else None,
        'qt_found_ip': hosts_elements[3] if 'hosts_elements' in locals() else None,
        'qt_found_host_filter': hosts_elements[4] if 'hosts_elements' in locals() else None,
        'qt_duplicate_host': hosts_elements[5] if 'hosts_elements' in locals() else None,
        'qt_all_hosts': hosts_elements[6] if 'hosts_elements' in locals() else None,
        'new_map': new_map if 'new_map' in locals() else None
    }
