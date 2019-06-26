import pyodbc
import json
from pymongo import MongoClient

ORIGEN = {
    "type": 'sql',
    "config": {
        "host": '172.18.1.41',
        "name": 'CPV2017_INDICADORES',
        "user": 'jramirez',
        "password": 'rjM3NLF8'
    },

    "table": 'JSON_FRECUENCIAS',
    #"table": '[FRECUENCIAS].[TEMATICA]',
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

    "collection": 'frecuencias2'
    #"collection": 'frecuencias_tematico'
}


#MAP = {
#    "cod_tematico": {
#        "type": "str",
#        "dest": "cod_tematico"
#    },
#
#    "cod_tipo_tematico": {
#        "type": "str",
#        "dest": "cod_tipo_tematico"
#    },
#
#    "descrip_tipo_tematico": {
#        "type": "str",
#        "dest": "descrip_tipo_tematico"
#    },
#
#    "categoria": {
#        "type": "str",
#        "dest": "categoria"
#    },
#
#    "clave_categoria": {
#        "type": "str",
#        "dest": "clave_categoria"
#    },
#    "subcategoria": {
#        "type": "str",
#        "dest": "subcategoria"
#    },
#
#    "indicador": {
#        "type": "str",
#        "dest": "indicador"
#    },
#
#    "cod_categoria": {
#        "type": "str",
#        "dest": "cod_categoria"
#    },
#
#    "cod_subcategoria": {
#        "type": "str",
#        "dest": "cod_subcategoria"
#    },
#
#    "codigo_subcategoria": {
#        "type": "str",
#        "dest": "codigo_subcategoria"
#    },
#    "cod_indicador": {
#        "type": "str",
#        "dest": "cod_indicador"
#    },
#    "cod_nivel_tematico": {
#        "type": "int",
#        "dest": "cod_nivel_tematico"
#    },
#    "orden": {
#        "type": "int",
#        "dest": "orden"
#    },
#    "titulo": {
#        "type": "str",
#        "dest": "titulo"
#    },
#    "cod_fuente": {
#        "type": "str",
#        "dest": "cod_fuente"
#    },
#    "buscador": {
#        "type": "str",
#        "dest": "buscador"
#    },
#    "es_cabecera": {
#        "type": "int",
#        "dest": "es_cabecera"
#    },
#    "activo": {
#        "type": "int",
#        "dest": "activo"
#    },
#
#}

MAP = {
    "cod_territorio": {
        "type": "str",
        "dest": "cod_territorio"
    },
    "ccdd": {
        "type": "str",
        "dest": "ccdd"
    },
    "ccpp": {
        "type": "str",
        "dest": "ccpp"
    },
    "ccdi": {
        "type": "str",
        "dest": "ccdi"
    },
    "departamento": {
        "type": "str",
        "dest": "departamento"
    },
    "provincia": {
        "type": "str",
        "dest": "provincia"
    },
    "distrito": {
        "type": "str",
        "dest": "distrito"
    },
    "titulo": {
        "type": "str",
        "dest": "titulo"
    },
    "cod_nivel": {
        "type": "int",
        "dest": "cod_nivel"
    },
    "edu": {
        "type": "json",
        "dest": "edu"
    },
    "pob": {
        "type": "json_group",
        "dest": "P01"
    },
    "hog": {
        "type": "json",
        "dest": "hog"
    },
    "sal": {
        "type": "json",
        "dest": "sal"
    },
    "viv": {
        "type": "json",
        "dest": "viv"
    },

}


def agrupar(datos):
    data = {}
    for k, v in datos.items():
        sp = str(k).split('_')
        print(sp)
        if len(sp) > 1:
            codigo = str(sp[0]).strip()
            tipo = str(sp[1]).lower()
            if codigo not in data:
                data[codigo] = {
                    "abs": None,
                    "porcent": None
                }
            data[codigo][tipo] = v
    return data


def to_dict(cursor, mapper):
    desc = [col[0] for col in cursor.description]
    datos = cursor.fetchall()
    stage_dict = [dict(zip(desc, dato)) for dato in datos]
    result_dict = []
    for dato in stage_dict:
        newdato = {}
        for k, v in dato.items():
            if k in mapper:
                if mapper[k]['type'] == 'str':
                    d = str(v).strip()
                elif mapper[k]['type'] == 'json_group':
                    if v is not None:
                        d = json.loads(v)
                        d = agrupar(d)
                    else:
                        d = {}
                elif mapper[k]['type'] == 'json':
                    if v is not None:
                        d = json.loads(v)
                    else:
                        d = v
                elif mapper[k]['type'] == 'int':
                    d = int(v) if v is not None else 0
                else:
                    d = v
                newdato[mapper[k]["dest"]] = d
        if newdato:
            result_dict.append(newdato)
    return result_dict


def mongo(ops, datos):
    config = ops['config']
    client = MongoClient(config['host'], config['port'])
    db = client[config["name"]]
    data = db[ops["collection"]].insert(datos)
    return data


def sql(ops, mapper):
    config = ops['config']
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                          % (config["host"], config["name"], config["user"], config["password"]))
    cursor = cnxn.cursor()
    query = "SELECT * FROM {}".format(ops['table'])
    cursor.execute(query)
    cabeceras = [col[0] for col in cursor.description]
    datos = to_dict(cursor, mapper)
    return datos


def run(*args):
    datos = sql(ORIGEN, MAP)
    data = mongo(DESTINO, datos)

