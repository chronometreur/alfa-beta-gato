"""
Paquete para arrancar y configurar la aplicacion
"""
from .util import Singleton, SingletonMeta
import yaml


# singleton Config para leer el archivo de configuracion en app/config
class Config(Singleton, metaclass=SingletonMeta):
    # llenar mi diccionario con el archivo de config
    def __init__(self, value: str):
        try:
            file = open(value, 'r')
            # cargar el contenido del archivo al diccionario
            self.__dict__ = yaml.load(file)
        except:
            print('No se puede abrir el archivo de configuracion')
