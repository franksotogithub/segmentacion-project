import pandas as pd, numpy as np
from django.db.models import Count
from django.core.cache import cache
from indicadores.models import FactIndicadores


def cachep_pivot(ubigeos):
    row = ['cod_tematico']
    column = ['ubigeo']
    data = ['valor', 'porcentaje']
    values = row + column + data
    categorias = ['01', '02', '03', '04', '05', '06']
    data_categoria = {}

    for c in categorias:
        indicadores = list(FactIndicadores.objects.filter(ubigeo__in=ubigeos, cod_categoria=c).values(*values))
        df = pd.DataFrame.from_records(indicadores)
        table = pd.pivot_table(df, values=data, index=row, columns=column, aggfunc=np.sum)
        table.columns = ['_'.join(col).lower() for col in table.columns]
        data_categoria[''.join(('P', c))] = table.reset_index().to_dict(orient="records")

    key = ''.join(ubigeos)
    cache.set(key, data_categoria, None)


def ubigeos(args):
    if 'nacional' in args:
        ubigeos = ['00']
        cachep_pivot(ubigeos)




def topivot(args):

    row = ['cod_tematico']
    column = ['ubigeo']
    data = ['valor', 'porcentaje']
    values = row + column + data
    indicadores = list(FactIndicadores.objects.filter(ubigeo__in=('00', '01', '02')).values(*values))
    df = pd.DataFrame.from_records(indicadores)
    table = pd.pivot_table(df, values=data, index=row, columns=column, aggfunc=np.sum)
    table.columns = ['_'.join(col).lower() for col in table.columns]
    datos = table.reset_index().to_dict(orient="records")
    print(table)

