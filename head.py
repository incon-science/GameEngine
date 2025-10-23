import pygame
from pygame.locals import *
import sys

pygame.init()

vec = pygame.math.Vector2 #2 for two dimensional

ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.display.set_caption("GameEngine") 

screen = pygame.display.set_mode((1920, 1080)) #mettre 0,0 pour plein ecran #,pygame.NOFRAME,32

infoObject = pygame.display.Info()

W_SCREEN = infoObject.current_w
H_SCREEN = infoObject.current_h

WIDTH = 1280/2
HEIGHT = 720/2

display_surf = pygame.Surface((WIDTH, HEIGHT))

charSheet = pygame.image.load("assets/AnimationSheet.png").convert_alpha()
#charSheet = pygame.transform.scale(charSheet,(charSheet.get_width()*4,charSheet.get_height()*4))

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()



