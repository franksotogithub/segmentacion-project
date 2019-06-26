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

    "table": '[PRINCIPALES].[TERRITORIO]',
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

    "collection": 'territorio'
}

MAP = {
    "COD_TERRITORIO": {
        "type": "str",
        "dest": "data"
    },
    "CCDD": {
        "type": "str",
        "dest": "ccdd"
    },
    "CCPP": {
        "type": "str",
        "dest": "ccpp"
    },

    "CCDI": {
        "type": "str",
        "dest": "ccdi"
    },

    "DEPARTAMENTO": {
        "type": "str",
        "dest": "departamento"
    },

    "PROVINCIA": {
        "type": "str",
        "dest": "provincia"
    },
    "DISTRITO": {
        "type": "str",
        "dest": "distrito"
    },
    "COD_NIVEL": {
        "type": "int",
        "dest": "index"
    },

    "PAIS": {
        "type": "str",
        "dest": "pais"
    },
    "REGION": {
        "type": "str",
        "dest": "region"
    },
    "BUSCADOR":{
        "type": "str",
        "dest": "buscador"
    },
    "TITULO":{
        "type": "str",
        "dest": "titulo"
    },
    "TERRITORIO_PADRE":{
        "type": "str",
        "dest": "territorio_padre"
    },
    "TERRITORIO_GRUPO":{
        "type": "str",
        "dest": "territorio_grupo"
    },
    "CODCCPP":{
        "type": "str",
        "dest": "codccpp"
    },
    "AREA":{
        "type": "str",
        "dest": "area"
    },
    "CENTRO_POBLADO":{
        "type": "str",
        "dest": "centro_poblado"
    },
    "COD_GRUPO":{
        "type": "str",
        "dest": "cod_grupo"
    },
    "TOTAL":{
        "type": "int",
        "dest": "total"
    },
    "imagen":{
        "type": "str",
        "dest": "imagen"
    },
    "flag_acceso_directo":{
        "type": "int",
        "dest": "flag_acceso_directo"
    },
    "LABEL_BUSCADOR":{
        "type": "str",
        "dest": "value"
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
    print(datos)
