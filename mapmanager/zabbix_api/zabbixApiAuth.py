import requests
from pyzabbix import ZabbixAPI, ZabbixAPIException

def authenticate(zbx_url, zbx_user, zbx_pass, zbx_api_token=None):
    requests.packages.urllib3.disable_warnings()

    zapi = ZabbixAPI(zbx_url)
    zapi.session.verify = False
    
    if zbx_api_token:
        print("\nTentando autenticação com token...\n")
        zapi.auth = zbx_api_token
        try:
            zapi.host.get(output=["hostid"], limit=1)
            print("Autenticado com sucesso via token!\n")
            return zapi
        except ZabbixAPIException:
            print("Token inválido. Tentando autenticação com login e senha...\n")
    
    try:
        zapi.login(user=zbx_user, password=zbx_pass)
        zapi.check_authentication()
        print("Autenticado com sucesso via usuário e senha!\n")
    except ZabbixAPIException as e:
        print(f"Não foi possível conectar na API do Zabbix. Erro: {e}\n")
        exit()
    
    return zapi