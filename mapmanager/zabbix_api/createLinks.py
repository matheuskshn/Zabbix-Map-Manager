def get_trigger(zapi, hostid, trigger_icmp, trigger_snmp):
    TRIGGER_DESCRIPTION1 = 'is unavailable by ICMP'
    TRIGGER_DESCRIPTION2 = 'SNMP not responding'

    trigger_data = zapi.trigger.get(hostids=hostid)
    triggerids = []

    if trigger_icmp:
        filtered_triggers = [trigger for trigger in trigger_data if TRIGGER_DESCRIPTION1 in trigger['description']]
        triggerids.append(filtered_triggers[0]['triggerid'] if filtered_triggers else None)

    if trigger_snmp:
        filtered_triggers = [trigger for trigger in trigger_data if TRIGGER_DESCRIPTION2 in trigger['description']]
        triggerids.append(filtered_triggers[0]['triggerid'] if filtered_triggers else None)
    
    return triggerids

def create_linktriggers(zapi, hostid1, hostid2, trigger_icmp, trigger_snmp):
    triggerids1 = get_trigger(zapi, hostid1, trigger_icmp, trigger_snmp)
    triggerids2 = get_trigger(zapi, hostid2, trigger_icmp, trigger_snmp)
    
    linktriggers = []

    for triggerid in triggerids1 + triggerids2:
        if triggerid:
            linktriggers.append({
                "triggerid": triggerid,
                "color": "DD0000",
                "drawtype": 0
            })
    
    return linktriggers

def create_links(elements, neighbors, zapi, trigger_icmp=False, trigger_snmp=False):
    element_dict = {str(element['elements'][0]['hostid']): element['selementid'] for element in elements}

    links = []
    
    for neighbor in neighbors:
        localHostID = neighbor['localHostID']
        neighborHostID = neighbor['neighborHostID']

        if localHostID in element_dict and neighborHostID in element_dict:
            selementid1 = element_dict[localHostID]
            selementid2 = element_dict[neighborHostID]

            linktriggers = []
            if trigger_icmp or trigger_snmp:
                linktriggers = create_linktriggers(zapi, localHostID, neighborHostID, trigger_icmp, trigger_snmp)

            link = {
                "selementid1": selementid1,
                "selementid2": selementid2,
                "color": "00CC00",
                'label': f"{neighbor['neighborPort']} - {neighbor['localPortName']}",
                "linktriggers": linktriggers
            }

            links.append(link)
    
    return links
