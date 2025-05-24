import pygame # klíčová knihovna umožňující vytvářet jednoduše nejen hry
pygame.init() # nutný příkaz hned na začátku pro správnou inicializaci knihovny
"""
class Player(pygame.sprite.Sprite):
    def __init__(self): #konstruktor
        super().__init__() #povolává z mrtvých konstruktor při vytvoření
        self.image = pygame.image.load("material/protofin_23_05_25.png")
        self.image = pygame.transform.scale(self.image, (500,600))
        self.rect = self.image.get_rect(midbottom = (100, 0.75*window_height))
"""
calculator_surface = pygame.image.load("material/protofin_23_05_25.png")
calculator_surface = pygame.transform.scale(calculator_surface, (500,600))



window_width = 500
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
while True:
    """
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
        """
    game_active = True                
    if game_active:            
        # pozadí
        screen.blit(calculator_surface,(0,0)) # položíme sky_surface na souřadnice [0,0]

    pygame.display.update() # updatujeme vykreslené okno
    clock.tick(60) # herní smyčka proběhne maximálně 60x za sekundu

