import re

INTERFACE_ABBREVIATIONS = {
    'FastEthernet': 'Fa',
    'GigabitEthernet': 'Gi',
    'TenGigabitEthernet': 'Te',
    'Wlan-GigabitEthernet': 'Wlan-Gi'
}

def get_items(zapi, hostids):
    cdp_items = zapi.item.get(
        output=['hostid', 'name', 'key_'],
        hostids=hostids,
        search={
            'key_': ['cdp.local.if.name.index','cdp.neighbor.name.index']
        },
        searchByAny= True,
    )
    
    return cdp_items

def get_neighbors(zapi, hosts_elements):
    hostids = [host['hostid'] for host in hosts_elements]
    cdp_items = get_items(zapi, hostids)

    host_dict = {host['host']: host['hostid'] for host in hosts_elements}

    data_dict = {}

    for host in cdp_items:
        localportindex_match = re.search(r'index\[([\d.]+)\]', host['key_'])
        if localportindex_match:
            localportindex = int(localportindex_match.group(1).split('.')[0])
            composite_key = f"{host['hostid']}-{localportindex}"

            if composite_key not in data_dict:
                data_dict[composite_key] = {
                    'localHostID': host['hostid'],
                    'localPortIndex': localportindex
                }

            if 'cdp.neighbor.name.index' in host['key_']:
                neighhost_match = re.search(r'neighborName\(([^)]+)\)', host['name'])
                neighport_match = re.search(r'DevicePort\(([^)]+)\)', host['name'])

                if neighhost_match:
                    neighbor_host_name_full = neighhost_match.group(1)
                    neighbor_host_name = re.match(r'^([^\.]+)', neighbor_host_name_full).group(1)
                    data_dict[composite_key]['neighborHost'] = neighbor_host_name
                    data_dict[composite_key]['neighborHostID'] = host_dict.get(neighbor_host_name, 'N/A')

                if neighport_match:
                    neighport_full = neighport_match.group(1)
                    for abbreviation, abbreviation_short in INTERFACE_ABBREVIATIONS.items():
                        if abbreviation in neighport_full:
                            data_dict[composite_key]['neighborPort'] = neighport_full.replace(abbreviation, abbreviation_short)
                            break
                    else:
                        data_dict[composite_key]['neighborPort'] = neighport_full

            elif 'cdp.local.if.name.index' in host['key_']:
                localportname_match = re.search(r'ifName\(([^)]+)\)', host['name'])
                if localportname_match:
                    localportname_full = localportname_match.group(1)
                    for abbreviation, abbreviation_short in INTERFACE_ABBREVIATIONS.items():
                        if abbreviation in localportname_full:
                            data_dict[composite_key]['localPortName'] = localportname_full.replace(abbreviation, abbreviation_short)
                            break
                    else:
                        data_dict[composite_key]['localPortName'] = localportname_full
                    
                    print (f"LOCALPORTNAME: {data_dict[composite_key]['localPortName']}")

    result_data = []

    for localportindex, data in data_dict.items():
        if data.get('neighborHost', 'N/A') != 'N/A':
            print(f"localHostID: {data['localHostID']}, neighborHost: {data.get('neighborHost', 'N/A')}, neighborHostID: {data.get('neighborHostID', 'N/A')}, neighborPort: {data.get('neighborPort', 'N/A')}, localPortIndex: {localportindex}, localPortName: {data.get('localPortName', 'N/A')}")
            result_data.append(data)
    # print(result_data)
    return result_data
