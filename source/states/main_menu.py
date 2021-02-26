#主菜单,静态封面

import pygame
from .. import setup
from .. import tools
from .. import constants as C
from .. components import info

class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info('main_menu')
        self.finished = False
        self.next = 'load_screen'


    def setup_background(self):
        self.setup_background = setup.GRAPHICS['level_1']
        self.setup_background_rect = self.setup_background.get_rect()
        self.setup_background = pygame.transform.scale(self.setup_background, (int(self.setup_background_rect.width * C.BG_MULTI),
                                                                               int(self.setup_background_rect.height * C.BG_MULTI)
                                                                               ))
        self.viewport = setup.SCREEN.get_rect()
        self.caption = tools.get_image(setup.GRAPHICS['title_screen'], 1, 60, 176, 88, (255, 0, 220), C.BG_MULTI)

    def setup_player(self):
        self.player_image = tools.get_image(setup.GRAPHICS['mario_bros'], 178, 32, 12, 16, (0,0,0), C.BG_MULTI)

    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = tools.get_image(setup.GRAPHICS['item_objects'], 24, 160, 8, 8, (0,0,0), C.BG_MULTI)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (220, 360)
        self.cursor.rect = rect
        self.cursor.state = '1P' # 状态机

    def update_cursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = '1P'
            self.cursor.rect.y = 360
        elif keys[pygame.K_DOWN]:
            self.cursor.state = '2P'
            self.cursor.rect.y = 405
        elif keys[pygame.K_RETURN]:
            if self.cursor.state == '1P':
                self.finished = True
            elif self.cursor.state == '2P':
                self.finished = True

    def update(self, surface, keys):
       self.update_cursor(keys)

       surface.blit(self.setup_background, self.viewport)
       surface.blit(self.caption, (170, 100))
       surface.blit(self.player_image, (110, 490))
       surface.blit(self.cursor.image, self.cursor.rect)

       self.info.update()
       self.info.draw(surface)