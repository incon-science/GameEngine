from classiq import *

P1 = Player()
all_sprites.add(P1)

PT01 = Platform((1000, 20),(0, 300))
all_sprites.add(PT01)
platforms.add(PT01)

while 1:

    if (P1.rect.y - camera.y) > HEIGHT*0.5:
        P1.respawn()

    P1.checkCollisions()


    for event in pygame.event.get():
        P1.controls(event)


    #fond noir
    display_surf.fill((50,50,50))

    #ajust camera
    camera.x = P1.pos.x - WIDTH/2
    camera.y = P1.pos.y - HEIGHT/2
    
    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        display_surf.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))


    #resize and blit surf on screen
    screen.blit(pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN)), (0,0))

    #show fps
    show_fps = Text(str(int(FramePerSec.get_fps())),(255,255,255),20,(20,15))
    show_fps.display(screen)

    pygame.display.update()
    FramePerSec.tick(FPS)