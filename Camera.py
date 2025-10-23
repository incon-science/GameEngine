from head import *

class Camera():
    def __init__(self):
        self.pos = vec((-WIDTH/2, -HEIGHT/2))

    def update(self,player):
        self.updateCameraCenterSmooth(player)

    def updateCameraCenterSmooth(self,player):
            camera_aim = vec(player.pos.x - WIDTH/2,player.pos.y - HEIGHT/2)

            camera_aim.x = round(camera_aim.x)
            camera_aim.y = round(camera_aim.y)

            if camera_aim.x > self.pos.x :
                self.pos.x += 1
            if camera_aim.x < self.pos.x :
                self.pos.x -= 1
            if camera_aim.y > self.pos.y :
                self.pos.y += 1
            if camera_aim.y < self.pos.y :
                self.pos.y -= 1