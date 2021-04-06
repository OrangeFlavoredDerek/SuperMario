import pygame
from .. import constants as C
from . import coin
from .. import tools, setup
pygame.font.init()

class Info:
    def __init__(self, state, game_info):
        self.state = state
        self.game_info = game_info
        self.create_state_labels()
        self.create_info_labels()
        self.flash_coin = coin.FlashingCoin()

    def create_state_labels(self):
        self.state_labels = []
        if self.state == 'main_menu':
            self.state_labels.append( (self.create_label( '1  PLAYER  GAME' ), (272, 360)) )
            self.state_labels.append( (self.create_label( '2  PLAYER  GAME' ), (272, 405)) )
            self.state_labels.append( (self.create_label( 'TOP - ' ), (290, 465)) )
            self.state_labels.append( (self.create_label( '000000' ), (400, 465)) )
        elif self.state == 'load_screen':
            self.state_labels.append( (self.create_label( 'WORLD' ), (280, 200)) )
            self.state_labels.append( (self.create_label( '1 - 1' ), (430, 200)) )
            self.state_labels.append( (self.create_label( 'X    {}'.format( self.game_info['lives'] ) ), (380, 280)) )
            self.player_image = tools.get_image( setup.GRAPHICS['mario_bros'], 178, 32, 12, 16, (0, 0, 0), C.BG_MULTI )
        elif self.state == 'game_over':
            self.state_labels.append( (self.create_label( 'GAME OVER' ), (280, 300)) )

    def create_info_labels(self):
        self.info_lables = []
        self.info_lables.append((self.create_label('MARIO'), (75, 30)))
        self.info_lables.append( (self.create_label( 'WORLD' ), (450, 30)))
        self.info_lables.append((self.create_label('TIME'), (625, 30)))
        self.info_lables.append( (self.create_label( '000000' ), (75, 55)))
        self.info_lables.append( (self.create_label( 'x00' ), (300, 55)))
        self.info_lables.append( (self.create_label( '1 - 1' ), (480, 55)))

    def create_label(self, label, size = 40, width_scale = 1.25, height_scale = 1):
        font = pygame.font.SysFont(C.FONT, size)
        label_image = font.render(label, 1, (255,255,255))
        rect = label_image.get_rect()
        label_image = pygame.transform.scale(label_image, (int(rect.width * width_scale),
                                             int(rect.height * height_scale)))

        return label_image

    def update(self):
        self.flash_coin.update()

    def draw(self, surface):
        for lable in self.state_labels:
            surface.blit(lable[0], lable[1])
        for lable in self.info_lables:
            surface.blit(lable[0], lable[1])
        surface.blit(self.flash_coin.image, self.flash_coin.rect)

        if self.state == 'load_screen':
            surface.blit(self.player_image, (300, 270))