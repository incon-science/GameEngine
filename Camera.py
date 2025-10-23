from head import *

class Camera():
    def __init__(self):
        self.pos = vec((-WIDTH/2, -HEIGHT/2))
        self.pos_aim = vec((-WIDTH/2, -HEIGHT/2))

    def update(self,player):
        self.pos_aim = vec(player.pos.x - WIDTH/2,player.pos.y - HEIGHT/2)
        self.updateCameraCenterSmooth()

    def updateCameraCenterSmooth(self):
        self.pos_aim.x = round(self.pos_aim.x)
        self.pos_aim.y = round(self.pos_aim.y)

        if self.pos_aim.x > self.pos.x :
            self.pos.x += 1
        if self.pos_aim.x < self.pos.x :
            self.pos.x -= 1
        if self.pos_aim.y > self.pos.y :
            self.pos.y += 1
        if self.pos_aim.y < self.pos.y :
            self.pos.y -= 1
