from .mapLog import log

def get_id(zapi, map_id=None, map_name=None):
    log("Iniciando busca pelo ID do mapa...")

    if map_id:
        existing_map_by_id = zapi.map.get(sysmapids=[map_id])
        if existing_map_by_id:
            log(f"Usando map_id fornecido: {map_id}")
            return map_id
        else:
            log(
                f"map_id fornecido {map_id} não encontrado. Procurando pelo nome do mapa..."
            )

    if map_name:
        existing_maps_by_name = zapi.map.get(filter={"name": map_name})
        if existing_maps_by_name:
            log(
                f"Mapa encontrado com o nome {map_name}. ID: {existing_maps_by_name[0]['sysmapid']}"
            )
            return existing_maps_by_name[0]["sysmapid"]

    log(f"Nenhum mapa encontrado com o nome {map_name}.")
    return None
