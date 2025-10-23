from head import *

class Camera():
    def __init__(self):
        self.camera = vec((-WIDTH/2, -HEIGHT/2))

    def update(self,player):
        self.updateCameraCenterSmooth(player)

    def updateCameraCenterSmooth(self,player):
            camera_aim = vec(player.pos.x - WIDTH/2,player.pos.y - HEIGHT/2)

            camera_aim.x = round(camera_aim.x)
            camera_aim.y = round(camera_aim.y)

            if camera_aim.x > self.camera.x :
                self.camera.x += 1
            if camera_aim.x < self.camera.x :
                self.camera.x -= 1
            if camera_aim.y > self.camera.y :
                self.camera.y += 1
            if camera_aim.y < self.camera.y :
                self.camera.y -= 1