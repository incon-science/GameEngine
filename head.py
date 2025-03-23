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
 
screen = pygame.display.set_mode((1920, 1080),pygame.NOFRAME,32)
pygame.mouse.set_visible(False) # Hide cursor here
pygame.display.set_caption("GameEngine")
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h

charSheet = pygame.image.load("assets/sprites/knight.png").convert_alpha()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()



