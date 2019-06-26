from .utils.sql_to_mongo import sql, mongo

ORIGEN = {
    "type": 'sql',
    "config": {
        "host": '172.18.1.41',
        "name": 'CPV2017_INDICADORES',
        "user": 'jramirez',
        "password": 'rjM3NLF8'
    },

    "table": '[CUADROS_ESTADISTICOS].[MAE_CUADROS]',
}

DESTINO = {
    "type": 'mongo',
    "config": {
        "host": '172.18.1.40',
        "name": 'RESULTADOSCPV',
        "user": '',
        "password": '',
        "port": 27017
    },

    "collection": 'estadisticos_cuadros'
}

MAP = {
    "cod_cuadro": {
        "type": "int",
        "dest": "cod_cuadro"
    },

    "tomo": {
        "type": "str",
        "dest": "tomo"
    },

    "titulo_cuadro": {
        "type": "str",
        "dest": "titulo_cuadro"
    },

    "nombre_cuadro": {
        "type": "str",
        "dest": "nombre_cuadro"
    },

    "pie_pagina": {
        "type": "str",
        "dest": "pie_pagina"
    },

    "filas": {
        "type": "json",
        "dest": "filas"
    }
}


def run(*args):
    datos = sql(ORIGEN, MAP, {})
    data = mongo(DESTINO, datos)
    print(datos)
