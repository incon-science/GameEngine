from Character import *
from Platform import *
from Text import *
from Player import *
from Camera import *


camera = Camera()

P1 = Player()
all_sprites.add(P1)

for i in range(-10,10):
    for j in range(-10,10):
        PT = Platform((16*10, 16),(i*j*16*12,j*16*5))
        all_sprites.add(PT)
        platforms.add(PT)
PT = Platform((20000, 200),(0,300))
all_sprites.add(PT)
platforms.add(PT)

while 1:

    P1.checkCollisions()

    for event in pygame.event.get():
        P1.controls(event)

    #fond noir
    display_surf.fill((50,50,50))

    #update camera
    camera.update(P1)
    
    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        display_surf.blit(entity.surf, (entity.rect.x - camera.camera.x, entity.rect.y - camera.camera.y))

    #resize and blit surf on screen
    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    #show fps
    show_fps = Text(str(int(FramePerSec.get_fps())),(255,255,255),20,(20,15))
    show_fps.display(screen)

    pygame.display.update()
    FramePerSec.tick(FPS)