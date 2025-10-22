from Character import *

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
            if event.key == pygame.K_SPACE:
                self.jump()
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_SPACE:
                self.cancel_jump()
 
