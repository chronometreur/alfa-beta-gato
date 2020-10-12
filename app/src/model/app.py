"""
Primero quiero un singleton para poder tener un archivo de configuraciones que se cargue solo una vez
Este buena practica la encontre en https://refactoring.guru/es/design-patterns/singleton/python/example#example-1
"""
from threading import Lock, Thread


# Implementacion del singleton con el metodo de la meta clase. Queda por
# descubrir por que el singleton ya no se usa en python
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


# mi clase que contendra mi configuracion
class Config(metaclass=SingletonMeta):
    pass
