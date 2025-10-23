from head import *
from scipy.interpolate import interp1d
import math

class Camera():
    def __init__(self):
        self.pos = vec((-WIDTH/2, -HEIGHT/2))
        self.pos_aim = vec((-WIDTH/2, -HEIGHT/2))

    def update(self,player):
        self.pos_aim = vec(player.pos.x - WIDTH/2,player.pos.y - HEIGHT/2)
        self.updateCameraCenterSmooth()

    def updateCameraCenterSmooth(self):

        """
        if self.pos_aim.x > self.pos.x :
            self.pos.x += 1
        if self.pos_aim.x < self.pos.x :
            self.pos.x -= 1
        if self.pos_aim.y > self.pos.y :
            self.pos.y += 1
        if self.pos_aim.y < self.pos.y :
            self.pos.y -= 1
        """

        print(self.pos_aim.x-self.pos.x) # -WIDTH/2 à WIDTH/2
        dif_x = self.pos_aim.x - self.pos.x

        offset = self.calculOffset(dif_x)

        self.pos.x += offset


    def calculOffset(self,diff_x):

        X = [-WIDTH/2,          -WIDTH/10,          0,          WIDTH/10,           WIDTH/2] # random x values
        Y = [-100,              -1,                 0,          1,                  100] # random y values

        # Finding the interpolation
        y_interp = interp1d(X, Y)

        rez = y_interp(diff_x)

        return math.floor(rez)