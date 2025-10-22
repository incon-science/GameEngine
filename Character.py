from CharacterAnimation import *

class Character(CharacterAnimation):
    def __init__(self):
        super().__init__() 
        self.surf = charSheet.subsurface((0,0,charSheet.get_width()/8,charSheet.get_height()/6))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False


    def move(self):
        self.acc = vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT] or pressed_keys[K_q] :
            self.acc.x = -ACC
            self.last_dir = -1
        if pressed_keys[K_RIGHT] or pressed_keys[K_d] :
            self.acc.x = ACC
            self.last_dir = 1
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
             
        self.rect.midbottom = self.pos

        self.animate()
 
    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15
           self.index_frame = 0
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def checkCollisions(self):
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:               
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False

    def respawn(self):
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.jumping = False
