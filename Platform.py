from head import *

class Platform(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((20,20,20))
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass