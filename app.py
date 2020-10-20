#!/usr/bin/env python3

from app.model.app import Config


"""
Ejecutamos la aplicacion
"""
if __name__ == "__main__":
    # 1. Creo mi singleton de configuracion
    config = Config(value='config/parameters.yml')
    print(config)
