from .utils.sql_to_mongo import sql, mongo

ORIGEN = {
    "type": 'sql',
    "config": {
        "host": '172.18.1.41',
        "name": 'CPV2017_INDICADORES',
        "user": 'jramirez',
        "password": 'rjM3NLF8'
    },

    "table": '[CUADROS_ESTADISTICOS].[MAE_CUADROS_DETALLE]',

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

    "collection": 'estadisticos_data2'
}

MAP = {
    "cod_cuadro": {
        "type": "int",
        "dest": "cod_cuadro"
    },

    "ubigeo": {
        "type": "str",
        "dest": "ubigeo"
    },

    "DATA": {
        "type": "json",
        "dest": "data"
    }
}


def run(*args):
    datos = sql(ORIGEN, MAP, {})
    print(datos)
    data = mongo(DESTINO, datos)
    print(datos)
