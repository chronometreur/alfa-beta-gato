"""
Mis adaptadores de vista
"""
from .util import Board


# Primero la libreria Turtle
class Turtle(Board):
    def board(self, size):
        print('Imprimiendo el tablero')
