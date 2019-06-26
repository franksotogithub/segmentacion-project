import pyodbc
import json
from pymongo import MongoClient

ORIGEN = {
    "type": 'sql',
    "config": {
        "host": '192.168.0.50\\MSSQLSERVER2016',
        "name": 'CPV_SEGMENTACION',
        "user": 'sa',
        "password": 'MBs0p0rt301'
    },

    "table": '[dbo].[SUBZONA]',
    "where" : " FASE='CPV2017' and ubigeo in ('150132','040104') "
    #"where" : " FASE='CPV2017' "
}

DESTINO = {
    "type": 'mongo',
    "config": {
        "host": 'localhost',
        "name": 'segmentacion',
        "user": '',
        "password": '',
        "port": 27017
    },

    "collection": 'subzonas'
}


MAP = {

    "ID": {
        "type": "str",
        "dest": "idsubzona"
    },

    "UBIGEO": {
        "type": "str",
        "dest": "ccdi"
    },
    "IDZONA": {
        "type": "str",
        "dest": "idzona"
    },


    "ZONA": {
        "type": "str",
        "dest": "zona"
    },

    "SUBZONA": {
        "type": "str",
        "dest": "subzona"
    },


    "CANT_VIV": {
        "type": "int",
        "dest": "cant_viv"
    },

    "RUTA_WEB":{
        "type": "str",
        "dest": "ruta_web"
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

    where=''

    if(ops['where']):
        where="where  {}".format(ops['where'])
    query = "SELECT * FROM {} {}".format(ops['table'],where)


    cursor.execute(query)
    cabeceras = [col[0] for col in cursor.description]
    datos = to_dict(cursor, mapper)
    return datos


def run(*args):
    datos = sql(ORIGEN, MAP)
    data = mongo(DESTINO, datos)
    print(datos)
