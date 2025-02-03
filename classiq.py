from head import *

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = charSheet.subsurface((0,0,charSheet.get_width()/8,charSheet.get_height()/9))
        self.rect = self.surf.get_rect()
   
        self.spawn = vec((0,0))
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.gauche = False
        self.droite = False

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        self.animation_frames = 4 #that define how many seconds or frames should pass before switching image.
        
    def update(self):
        self.checkCollisions()

        self.acc = vec(0,0.5)
                
        if self.gauche:
            self.acc.x = -ACC
        if self.droite:
            self.acc.x = ACC
                 
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
        self.rect = self.surf.get_rect()
   
        self.spawn = vec((0,0))
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.gauche = False
        self.droite = False

    def animate(self):
        if self.jumping :
            self.jumpAnimation()
        elif self.droite or self.gauche:
            self.runAnimation()
        else :
            self.index_frame = 0
            self.idleAnimation()

    def jumpAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,charSheet.get_height()/9*5,charSheet.get_width()/8,charSheet.get_height()/9))

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 8 :
                self.index_frame = 0  

    def runAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,charSheet.get_height()/9*3,charSheet.get_width()/8,charSheet.get_height()/9))
        if self.gauche:
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 8 :
                self.index_frame = 0  

    def idleAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,0,charSheet.get_width()/8,charSheet.get_height()/9))

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 2 :
                self.index_frame = 0  

class Player(Character):
    def __init__(self):
        super().__init__()  

    def controls(self,event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.gauche = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite = True  
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.jump()
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.gauche = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite = False 
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.cancel_jump()

        if event.type == pygame.JOYBUTTONDOWN:      
            if  event.button == 4:
                self.gauche = True
            if  event.button == 5:
                self.droite = True  
            if  event.button == 0:
                self.jump()
        if event.type == pygame.JOYBUTTONUP:      
            if  event.button == 4:
                self.gauche = False
            if  event.button == 5:
                self.droite = False 
            if  event.button == 0:
                self.cancel_jump()

        self.joystick()

    def joystick(self):
        if pygame.joystick.get_count()>0:
            axis_pos = joysticks[0].get_axis(0)

            if axis_pos < -1 * deadzone:
                self.gauche = True
            elif axis_pos > deadzone:
                self.droite = True  
            else:
                self.gauche = False
                self.droite = False          
 
class Platform(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass
