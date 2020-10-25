"""
Mis adaptadores de vista
"""
import pygame
from .util import Board


# Con la libreria Turtle
class Turtle(Board):
    def print_board(self, size):
        print('Imprimiendo el tablero')


# Con la libreria Pygame
class Pygame(Board):
    def __init__(self):
        pygame.init()

    def init(self, data):
        self.__dict__ = data
        self.__set_size__()
        self.__control__()

    def print_board(self, size):
        print('Imprimiendo el tablero PyGame')

    def __control__(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()

    def __set_size__(self):
        size = self.__dict__['length'], self.__dict__['width']
        self.screen = pygame.display.set_mode(size)
