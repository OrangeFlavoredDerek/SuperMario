# 游戏启动代码

import pygame
from . import constants as C
from . import tools

#初始化屏幕
pygame.init()
SCREEN = pygame.display.set_mode( (C.SCREEN_W, C.SCREEN_H) )

GRAPHICS = tools.load_graphics('resources/graphics')
