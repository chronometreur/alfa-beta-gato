#!/usr/bin/env python3

from app.model.app import Config
from app.model.util import Factory


"""
Ejecutamos la aplicacion
"""
if __name__ == "__main__":
    # 1. Creo mi singleton de configuracion y mi singleton fabrica
    config = Config('config/config.yml')
    factory = Factory()

    # 2. Obtengo mi front
    front = factory.get_object('view.front.{}'.format(config.view))    # mayuscula la ultima parte
    front.board(config.size)
