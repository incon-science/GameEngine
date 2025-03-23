from head import *

class Platform(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.surf = platformSheet.subsurface((0,0,platformSheet.get_width()/4,platformSheet.get_height()/4))
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass
