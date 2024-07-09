# Zabbix Map Manager

Este projeto é uma aplicação Django para gerenciar mapas do Zabbix.

## Requisitos

- Python 3.11
- Pip

## Instalação

1. Clone o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd zabbix_map_manager
    ```

2. Crie um ambiente virtual usando `venv`:
    ```bash
    python3.11 -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Copie o arquivo de configuração:

    - Copie o arquivo `config-example.py` para `config.py`:
        ```bash
        cp zabbix_api/config-example.py zabbix_api/config.py
        ```

5. Configure o banco de dados (SQLite por padrão):
    - Execute as migrações para recriar o banco de dados:
        ```bash
        python3 manage.py migrate
        ```

6. Crie um superusuário para acessar a administração do Django:
    ```bash
    python3 manage.py createsuperuser
    ```

7. Configure a aplicação:

    - Edite o arquivo `zabbix_api/config.py` para incluir as configurações de autenticação da API do Zabbix:
        ```python
        # URL para a API do Zabbix.
        ZABBIX_URL = 'https://localhost.com/'
        # URL com caminho da api.
        ZABBIX_API_URL = f"{ZABBIX_URL}api_jsonrpc.php"
        # Nome de usuário para autenticação na API do Zabbix.
        ZABBIX_USER = "user"
        # Senha para autenticação na API do Zabbix.
        ZABBIX_PASSWORD = "pass"
        # Token de API para autenticação segura.
        ZABBIX_API_TOKEN = ""
        ```

    - Nesse mesmo arquivo, `config.py`, você encontrará configurações adicionais para a criação de mapas.

8. Inicie o servidor de desenvolvimento:
    ```bash
    python3 manage.py runserver
    ```

9. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:8000/mapmanager/create-map/
    ```

## Estrutura do Projeto

- `mapmanager/`: Contém a aplicação principal.
- `zabbix_api/`: Contém a integração com a API do Zabbix.
- `ZabbixMap/`: Contém as configurações do projeto Django.
- `static/ZabbixMap/image/`: Contém arquivos estáticos, como ícones.
- `templates/`: Contém templates HTML.
- `manage.py`: Script para executar comandos do Django.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.