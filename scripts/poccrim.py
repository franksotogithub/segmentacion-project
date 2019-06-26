from .utils.sql_to_mongo import sql, mongo

ORIGEN = {
    "type": 'sql',
    "config": {
        "host": '172.18.1.41',
        "name": 'DATACRIM2019_BDPOC',
        "user": 'usr_criminalidad',
        "password": 'skUFqDilUT'
    },

    "table": 'TMP_JSON_ARBOL_TEMATICO',
}

DESTINO = {
    "type": 'mongo',
    "config": {
        "host": '172.18.1.40',
        "name": 'poc_datacrim',
        "user": '',
        "password": '',
        "port": 27017
    },

    "collection": 'menu_principal'
}

MAP = {
    "id": {
        "type": "int",
        "dest": "id"
    },
    "json_arbol": {
        "type": "json",
        "dest": "data"
    }
}


def run(*args):
    datos = sql(ORIGEN, MAP, {})
    # print(datos)
    new_datos = []
    for dato in datos:
        # print(dato['data'])
        new_datos.append(dato['data'])
    # print(new_datos)
    data = mongo(DESTINO, new_datos)
    # print(datos)
