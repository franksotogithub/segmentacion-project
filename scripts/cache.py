from .utils.ubigeos import *


def run(*args):
    if 'ubigeos' in args:
        ubigeos(args)

    elif 'pivot' in args:
        topivot(args)
