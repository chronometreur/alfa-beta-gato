"""
Paquete para arrancar y configurar la aplicacion
"""
import traceback
import yaml

from .util import Singleton, SingletonMeta


# singleton Config para leer el archivo de configuracion en app/config
class Config(Singleton, metaclass=SingletonMeta):
    # llenar mi diccionario con el archivo de config
    def __init__(self, value: str):
        file = open(value, 'r')
        self.__dict__ = yaml.load(file)
