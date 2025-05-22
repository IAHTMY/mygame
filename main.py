import pygame # klíčová knihovna umožňující vytvářet jednoduše nejen hry
import random
pygame.init() # nutný příkaz hned na začátku pro správnou inicializaci knihovny

class Player(pygame.sprite.Sprite):
    def __init__(self): #konstruktor
        super().__init__() #povolává z mrtvých konstruktor při vytvoření
        self.image = pygame.image.load("material/tryoutimage.png")
        self.image = pygame.transform.scale(self.image, (50,150))
        self.rect = self.image.get_rect(midbottom = (100, 0.75*window_height))

window_width = 800
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))

while True:
    # zjistíme co dělá hráč za akci
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # zavřeme herní okno
            exit() # úplně opustíme herní smyčku, celý program se ukončí
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active == False: #Game over stav
                    game_active = True
                else:
                    game_active = True
                    
    if game_active:            
        # pozadí
        screen.blit(sky_surface,(0,0)) # položíme sky_surface na souřadnice [0,0]
        screen.blit(ground_surface,(0,0.75*window_height)) # položíme ground_surface na souřadnice [0,300] (pod oblohu)
        screen.blit(score_surface, score_rect)

        
        if counter > 120:
            counter = 0
            obstacles_group.add(Obstacle())
            
        else:
            counter += 1
        # nepřítel
        obstacles_group.draw(screen)
        obstacles_group.update()

        #hráč
        player.draw(screen)
        player.update()

        count += 1
        score_surface = text_font.render(f"Skore: {count // 60}", True, "Black") # text, anti-aliasing, černá barva písma
        score_rect = text_surface.get_rect(center=(window_width/2, window_height/2)) # kam se to má vykreslit

        game_active = is_collision() #byla kolize?
        
    else:
        screen.blit(sky_surface,(0,0))
        screen.blit(text_surface, text_rect)
        count = 0
    pygame.display.update() # updatujeme vykreslené okno
    clock.tick(60) # herní smyčka proběhne maximálně 60x za sekundu

