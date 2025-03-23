from CharacterAnimation import *

class Character(CharacterAnimation):
    def __init__(self):
        super().__init__() 
   
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

        self.animate()
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
             
        self.rect.midbottom = self.pos

    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -10
           self.index_frame = 0
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def checkCollisions(self):
        if self.vel.y > 0:    
            collide = pygame.sprite.spritecollide(self, platforms, False, pygame.sprite.collide_mask)
            if collide:
                if self.rect.bottom < collide[0].rect.bottom:               
                    self.pos.y = collide[0].rect.top +4
                    self.vel.y = 0
                    self.jumping = False

    def respawn(self):
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.jumping = False
