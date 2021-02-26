from ..components import info
import pygame


class Level:
    def __init__(self):
        self.finished = False
        self.next = None

    def update(self, surface, keys):
        self.draw( surface )

    def draw(self, surface):
        surface.fill( (0, 255, 0) )# 绿色
