# URL para a API do Zabbix.
ZABBIX_URL = 'https://localhost.com/'
ZABBIX_API_URL = f"{ZABBIX_URL}api_jsonrpc.php"
# Nome de usuário para autenticação na API do Zabbix.
ZABBIX_USER = "user"
# Senha para autenticação na API do Zabbix.
ZABBIX_PASSWORD = "pass"
# Token de API para autenticação segura.
ZABBIX_API_TOKEN = ""

# Configurações padrões do mapa:
USERID=1 # Usuário admin
BACKGROUNDID=323
EXPANDPROBLEM=0
EXPANDMACROS=1
MARKELEMENTS=1
SHOW_SUPPRESSED=1
SEVERITY_MIN=2
HIGHLIGHT=0
LABEL_TYPE=0
PRIVATE=0

# Mapeamento de icones por de tipos de host, definido pelo nome do equipamento.
ICON_MAP = {
    # A chave é o filtro de pesquisa (hostname) que determina o conjunto de icones.
    # Caso necessário adicione um novo filtro abaixo, seguindo o padrão:
    # "FILTRO": ["iconid_off", "iconid_on", "iconid_disabled", "iconid_maintenance"]
    #
    # ORDEM: "ICONID_OFF", "ICONID_ON", "ICONID_DISABLED", "ICONID_MAINTENANCE"
    "CORESW": ["371", "372", "0", "370"],  # sw-l3-64
    "SW-CORE": ["371", "372", "0", "370"],  # sw-l3-64
    "PYYZ": ["371", "372", "0", "370"],  # sw-l3-64
    "RS0": ["371", "372", "0", "370"],  # sw-l3-64
    "RS1": ["371", "372", "0", "370"],  # sw-l3-64
    "ACCSSW": ["368", "369", "0", "367"],  # sw-l2-64
    "SW0": ["368", "369", "0", "367"],  # sw-l2-64
    "SW1": ["368", "369", "0", "367"],  # sw-l2-64
    "WAN": ["401", "402", "0", "400"],  # service-router-64
    "WA0": ["401", "402", "0", "400"],  # service-router-64
    "RT0": ["401", "402", "0", "400"],  # service-router-64
    "GK0": ["401", "402", "0", "400"],  # service-router-64
    "AP": ["329", "330", "0", "328"],  # ap-64
    "WP": ["329", "330", "0", "328"],  # ap-64
    "CAMERA": ["188", "189", "0", "535"],  # cam-64
    "CFTV": ["188", "189", "0", "535"],  # cam-64
    "VOIP": ["423", "421", "0", "422"],  # voice-gateway-64
    "FW0": ["542", "541", "0", "540"],  # firewall-64
    "VALEVA": ["542", "541", "0", "540"],  # firewall-64
    "WC0": ["354", "353", "0", "352"],  # control-wireless-64
    "WC1": ["354", "353", "0", "352"],  # control-wireless-64
    "MGMTP": ["160", "160", "0", "160"],  # UPS_64
    "HF-DCA-VD": ["419", "420", "0", "418"],  # virtual_server64
    "HF-DCA-VS": ["419", "420", "0", "418"],  # virtual_server64
    "HF-DTO-VD": ["419", "420", "0", "418"],  # virtual_server64
    "HF-DTO-VS": ["419", "420", "0", "418"],  # virtual_server64
}

# IDs de ícones padrão
DEFAULT_ICONS = ["594", "593", "0", "595"]  # ip-device-64
