from head import *

class CharacterAnimation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.last_dir = 0 #-1 left 1 right

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        
        self.current_animation = "idle"

    def resetAnimation(self):
        self.index_frame = 0
        self.current_frame = 0

    def animate(self):
        if self.jumping :
            if self.current_animation != "jump":
                self.resetAnimation()
            self.current_animation = "jump"

            self.jumpAnimation()

        elif self.vel.x != 0:
            if self.current_animation != "run":
                self.resetAnimation()
            self.current_animation = "run"

            self.runAnimation()

        else :
            if self.current_animation != "idle":
                self.resetAnimation()
            self.current_animation = "idle"

            self.idleAnimation()

    def jumpAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,charSheet.get_height()/6*3,charSheet.get_width()/8,charSheet.get_height()/6))
        if self.last_dir < 0 :
                    self.surf = pygame.transform.flip(self.surf, True, False)
                    
        self.current_frame += 1
        if self.current_frame >= 12:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 8 :
                self.index_frame = 0  

    def runAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*4+charSheet.get_width()/8*self.index_frame,charSheet.get_height()/6*1,charSheet.get_width()/8,charSheet.get_height()/6))
        if self.last_dir < 0:
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 12:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 4 :
                self.index_frame = 0  

    def idleAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame,0,charSheet.get_width()/8,charSheet.get_height()/6))
        if self.last_dir < 0 :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame += 1
        if self.current_frame >= 12:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 2 :
                self.index_frame = 0  



