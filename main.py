from classiq import *

P1 = Player()
all_sprites.add(P1)

PT01 = Platform((500, 10),(0, 50))
all_sprites.add(PT01)
platforms.add(PT01)


while 1:

    P1.checkCollisions()

    for event in pygame.event.get():
        P1.controls(event)

    if (P1.rect.y - camera.y) > H_SURF*0.5:
        P1.respawn()


    #fond noir
    display_surf.fill((50,50,50))

    #ajust camera
    camera.x = P1.pos.x - W_SURF/2
    camera.y = P1.pos.y - H_SURF/2

    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        display_surf.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

    display_surf = pygame.transform.scale(display_surf, (W_SCREEN, H_SCREEN))
    screen.blit(display_surf, (0,0))

    pygame.display.update()
    FramePerSec.tick(FPS)