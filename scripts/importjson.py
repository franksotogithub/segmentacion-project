import  json
import pprint
import os
from pymongo import  MongoClient
from resultados.settings.base import  BASE_DIR


DESTINO = {
    "type": 'mongo',
    "config": {
        "host": '172.18.1.40',
        #"host": 'localhost',
        "name": 'RESULTADOSCPV',
        "user": '',
        "password": '',
        "port": 27017
    },
    "collection": 'departamentos'
}

ORIGEN ={
    'filename': os.path.join(BASE_DIR,'fixtures','departamento.geojson')
}

def mongo(ops, datos):
    config = ops['config']
    client = MongoClient(config['host'], config['port'])
    db = client[config["name"]]
    data = db[ops["collection"]].insert_many(datos)
    return data

def get_datos(ops):
    data = open(ops['filename'])
    datos=json.load(data)["features"]
    return datos
def run(*args):
    datos = get_datos(ORIGEN)
    data = mongo(DESTINO, datos)
    print(datos)
