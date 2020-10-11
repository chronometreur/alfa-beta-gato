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

    def __call__(self, *args, **kwargs):
        pass