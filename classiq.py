from head import *

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = charSheet.subsurface((0,0,charSheet.get_width()/8,charSheet.get_height()/9))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.last_dir = 0

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        
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

    def animate(self):
        if self.jumping :
            self.jumpAnimation()
        elif self.acc.x != 0:
            self.runAnimation()
        else :
            self.idleAnimation()

    def jumpAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,charSheet.get_height()/9*5,charSheet.get_width()/8,charSheet.get_height()/9))

        self.current_frame += 1
        if self.current_frame >= 6:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 8 :
                self.index_frame = 0  

    def runAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,charSheet.get_height()/9*3,charSheet.get_width()/8,charSheet.get_height()/9))
        if self.acc.x < 0:
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 4:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 8 :
                self.index_frame = 0  

    def idleAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,0,charSheet.get_width()/8,charSheet.get_height()/9))
        if self.last_dir < 0 :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 18:
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
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.jump()
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.cancel_jump()

        '''
        if event.type == pygame.JOYBUTTONDOWN:      
            if  event.button == 0:
                self.jump()
        if event.type == pygame.JOYBUTTONUP:      
            if  event.button == 0:
                self.cancel_jump()

        if pygame.joystick.get_count()>0:
            axis_pos = joysticks[0].get_axis(0)

            if axis_pos < -1 * deadzone:
                self.vel.x = -VEL
                self.last_dir = -1
            elif axis_pos > deadzone:
                self.vel.x = VEL
                self.last_dir = 1
            else:
                self.vel.x = 0      '''  
 
class Platform(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((20,20,20))
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass


class Text(pygame.sprite.Sprite):
    def __init__(self,txt,color,size,pos, font = 'Lucida Console'):
        super().__init__()  

        my_font = pygame.font.SysFont(font, size)
        self.surf = my_font.render(txt, True, color)
        self.rect = self.surf.get_rect(center = pos)

    def display(self,surf):
        surf.blit(self.surf, self.rect)