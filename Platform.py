from head import *
from random import randrange

class Platform(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        x = randrange(4)
        self.surf = platformSheet.subsurface((0,platformSheet.get_height()/4*x,platformSheet.get_width()/4,platformSheet.get_height()/4))
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass
