# 工具和游戏主控

import pygame
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.display.quit()
            elif event.type == pygame.KEYDOWN:
               self.keys = pygame.key.get_pressed()
            elif event.type == pygame.KEYUP:
               self.keys = pygame.key.get_pressed()
          self.screen.fill((random.randint(0, 225), random.randint(0, 225), random.randint(0, 225)))#随机颜色(0~225)
          pygame.display.update()
          self.clock.tick(60)# 游戏帧数

