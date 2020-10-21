"""
Paquete de clases de utilerias
"""
import app.view.front
import importlib
from threading import Lock


# Implementacion del singleton con el metodo de la meta clase. Queda por descubrir por que el singleton ya no se usa en
# python. Esto lo encontre en https://refactoring.guru/es/design-patterns/singleton/python/example#example-1
class SingletonMeta(type):
    _instances = {}
    # objeto lock que se usara para sincronizar los hilos cuando se llame al singleton
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        # imagina que el programa recien arranca. Como todavia no hay instancia en el singleton, varios hilos pueden
        # llegar a este punto casi al mismo tiempo. El primero entrara y bloqueara y el resto tendran que esperar
        with cls._lock:
            # el primer hilo entra y crea la instancia singleton. Al terminar, otro posible hilo que este esperando
            # entra a esta seccion pero como el singleton ya esta inicializado no se creara un nuevo objeto
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


# clase singleton para manipular el diccionario interno
class Singleton(metaclass=SingletonMeta):
    def __getattr__(self, item):
        return getattr(self.__dict__, item)


# Fabrica. La idea era generar el nombre de la clase en una string como en PHP, pero creo que en Python no se puede
# Lo que voy a hacer es registrar todos mis creadores, cada uno especializado en una subclase
class Factory(Singleton, metaclass=SingletonMeta):
    # Metodo creador
    def get_object(self, key):
        key = 'app.' + key
        point = key.rfind('.')
        m = key[:point]
        c = key[point + 1:].capitalize()
        module = importlib.import_module(m)
        declaration = getattr(module, c)

        return declaration()
