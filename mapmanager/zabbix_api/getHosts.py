def get_hosts(zapi, map_groups, map_hosts, map_ips, map_hosts_filter):

    add_groups = []
    add_hosts = []
    add_ips = []
    add_filter_hosts = []

    get_all_hosts = zapi.host.get(output=['hostid', 'host'], selectInterfaces=['ip'], selectGroups=['groupid'])

    if map_groups:
        hosts_groups = zapi.hostgroup.get(filter={"name": map_groups})
        group_ids = {group['groupid'] for group in hosts_groups}
        add_groups = [host for host in get_all_hosts if any(group['groupid'] in group_ids for group in host['groups'])]
    else:
        add_groups = []

    count_groups = len(add_groups)

    if map_hosts:
        host_names_set = set(map_hosts.split(", ")) if isinstance(map_hosts, str) else set(map_hosts)
        add_hosts = [host for host in get_all_hosts if host['host'] in host_names_set]
    else:
        add_hosts = []

    count_hosts = len(add_hosts)
    
    if map_ips:
        ip_set = set(map_ips.split(", ")) if isinstance(map_ips, str) else set(map_ips)
        add_ips = [host for host in get_all_hosts if any(interface['ip'] in ip_set for interface in host['interfaces'])]
    else:
        add_ips = []

    count_ips = len(add_ips)
    
    if map_hosts_filter:
        if isinstance(map_hosts_filter, list):
            map_hosts_filter = ", ".join(map_hosts_filter)
        host_filters_set = set(map_hosts_filter.split(", "))
        add_filter_hosts = [host for host in get_all_hosts if any(host['host'].startswith(filter_str) for filter_str in host_filters_set)]
    else:
        add_filter_hosts = []
        
    count_filter_hosts = len(add_filter_hosts)

    seen = set()
    all_hosts = []
    for host in add_groups + add_hosts + add_ips + add_filter_hosts:
        host_id = host['hostid']
        if host_id not in seen:
            host.pop('groups', None)
            host.pop('interfaces', None)
            all_hosts.append(host)
            seen.add(host_id)
    
    count_map_all_hosts = len(all_hosts)
    
    count_duplicates_hosts = (count_groups + count_hosts + count_ips + count_filter_hosts) - count_map_all_hosts
    
    return all_hosts, count_groups, count_hosts, count_ips, count_filter_hosts, count_duplicates_hosts, count_map_all_hosts
