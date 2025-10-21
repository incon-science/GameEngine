import pygame
from pygame.locals import *
import random
import sys

pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional

ACC = 0.5
FRIC = -0.12
FPS = 60

deadzone = 0.3#for joystick
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((0, 0),pygame.NOFRAME,32)
pygame.mouse.set_visible(False) # Hide cursor here
pygame.display.set_caption("GameEngine")
infoObject = pygame.display.Info()



W_SCREEN = infoObject.current_w
H_SCREEN = infoObject.current_h

WIDTH = 1920
HEIGHT = 1080
display_surf = pygame.Surface((WIDTH, HEIGHT))

charSheet = pygame.image.load("assets/AnimationSheet.png").convert_alpha()
charSheet = pygame.transform.scale(charSheet,(charSheet.get_width()*4,charSheet.get_height()*4))

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()



