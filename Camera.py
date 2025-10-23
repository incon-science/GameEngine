from head import *
from scipy.interpolate import interp1d
import math

class Camera():
    def __init__(self):
        self.pos = vec((-WIDTH/2, -HEIGHT/2))
        self.pos_aim = vec((-WIDTH/2, -HEIGHT/2))

    def update(self,player):
        self.pos_aim = vec(player.pos.x - WIDTH/2,player.pos.y - HEIGHT/2)
        
        if player.moved_left :
            self.pos_aim.x -= WIDTH/20
        else :
            self.pos_aim.x += WIDTH/20

        self.updateCameraCenterSmooth()

    def updateCameraCenterSmooth(self):
        dif_x = self.pos_aim.x - self.pos.x
        offset_x = self.calculOffsetX(dif_x)
        self.pos.x += offset_x

        dif_y = self.pos_aim.y - self.pos.y
        offset_y = self.calculOffsetY(dif_y)
        self.pos.y += offset_y

    def calculOffsetX(self,diff_x):

        X = [-WIDTH/2, 0, WIDTH/2] # random x values
        Y = [-40, 0, 40] # random y values

        # Finding the interpolation
        y_interp = interp1d(X, Y)

        rez = y_interp(diff_x)

        return math.floor(rez)

    def calculOffsetY(self,diff_y):

        X = [-HEIGHT/2, 0, HEIGHT/2] # random x values
        Y = [-40, 0, 40] # random y values

        # Finding the interpolation
        y_interp = interp1d(X, Y)

        rez = y_interp(diff_y)

        return math.floor(rez)