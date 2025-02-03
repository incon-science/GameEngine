from classiq import *

def game():
    P1 = Player()
    all_sprites.add(P1)

    PT01 = Platform((1500, 20),(0, 300))
    all_sprites.add(PT01)
    platforms.add(PT01)

    while 1:

        for event in pygame.event.get():
            P1.controls(event)

        #fond noir
        screen.fill((50,50,50))

        #ajust camera
        camera.x = P1.pos.x - WIDTH/2
        camera.y = P1.pos.y - HEIGHT/2
        
        #deplacer les sprites 
        for entity in all_sprites:
            entity.update()
            screen.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

        if (P1.rect.y - camera.y) > HEIGHT:
            P1.respawn()

        pygame.display.update()
        FramePerSec.tick(FPS)