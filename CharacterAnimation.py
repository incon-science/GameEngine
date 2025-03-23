from head import *

class CharacterAnimation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.surf = charSheet.subsurface((0,0,charSheet.get_width()/8,charSheet.get_height()/8))
        self.rect = self.surf.get_rect()

        self.last_dir = 0

        self.index_frame_idle = 0 #that keeps track on the current index of the image list.
        self.current_frame_idle = 0 #that keeps track on the current time or current frame since last the index switched. 

        self.index_frame_run = 0 #that keeps track on the current index of the image list.
        self.current_frame_run = 0 #that keeps track on the current time or current frame since last the index switched. 

        self.index_frame_roll = 0 #that keeps track on the current index of the image list.
        self.current_frame_roll = 0 #that keeps track on the current time or current frame since last the index switched. 

        self.index_frame_hit = 0 #that keeps track on the current index of the image list.
        self.current_frame_hit = 0 #that keeps track on the current time or current frame since last the index switched. 

        self.index_frame_death = 0 #that keeps track on the current index of the image list.
        self.current_frame_death = 0 #that keeps track on the current time or current frame since last the index switched. 

    def animate(self):
        if self.acc.x != 0:
            self.runAnimation()
        else :
            self.idleAnimation()

    def runAnimation(self):
        if self.index_frame_run >= 8:
            self.surf = charSheet.subsurface((charSheet.get_width()/8*(self.index_frame_run-8),charSheet.get_height()/8*3,charSheet.get_width()/8,charSheet.get_height()/8))
        else :
            self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame_run,charSheet.get_height()/8*2,charSheet.get_width()/8,charSheet.get_height()/8))

        if self.last_dir < 0 :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame_run += 1
        if self.current_frame_run >= NB_FRAMES_SWITCH:
            self.current_frame_run = 0
            self.index_frame_run += 1
            if self.index_frame_run >= 16 :
                self.index_frame_run = 0  

    def idleAnimation(self):
        self.surf = charSheet.subsurface((charSheet.get_width()/8*self.index_frame_idle,charSheet.get_height()/8*0,charSheet.get_width()/8,charSheet.get_height()/8))

        if self.last_dir < 0 :
            self.surf = pygame.transform.flip(self.surf, True, False)

        self.current_frame_idle += 1
        if self.current_frame_idle >= NB_FRAMES_SWITCH:
            self.current_frame_idle = 0
            self.index_frame_idle += 1
            if self.index_frame_idle >= 4 :
                self.index_frame_idle = 0  
