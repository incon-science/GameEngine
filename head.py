import pygame
from pygame.locals import *
import random
import sys

def nettoyage():
    pygame.sprite.Group.empty(all_sprites)
    pygame.sprite.Group.empty(platforms)

pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional

ACC = 0.5
FRIC = -0.06#-0.12
FPS = 60

deadzone = 0.3#for joystick
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((0, 0),pygame.NOFRAME,32)
pygame.mouse.set_visible(False) # Hide cursor here
pygame.display.set_caption("Zeldo")
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h

runSheet = pygame.image.load("assets/_Run.png").convert_alpha()
runSheet = pygame.transform.scale(runSheet,(1200*2,80*2))

idleSheet = pygame.image.load("assets/_Idle.png").convert_alpha()
idleSheet = pygame.transform.scale(idleSheet,(1200*2,80*2))

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
