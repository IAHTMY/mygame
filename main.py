import pygame # klíčová knihovna umožňující vytvářet jednoduše nejen hry
pygame.init() # nutný příkaz hned na začátku pro správnou inicializaci knihovny

fronta = []
obrazovka = None
answer = None

# IKONA
calcicon = pygame.image.load("material/calcicon.png")  # Make sure the image is in the same directory
pygame.display.set_icon(calcicon)

# JMENO HRY
pygame.display.set_caption("Kalkulačka Gasio 123")

# FONT 
color_set = ["Black", "Blue", "Green", "Yellow", "Red", "Black"]
color_index = 0
if color_index == 5:
    color_index = 0
color = color_set[color_index]
text_font = pygame.font.Font("material/techfont.ttf",50) # 100 je velikost písma
text_surface = text_font.render(f"{obrazovka}", True, color) # text, anti-aliasing, černá barva písma
text_rect = text_surface.get_rect(62, 62) # kam se to má vykreslit

# HUDBA
bg_music = pygame.mixer.Sound("material/music/elevator.mp3")
bg_music.play(loops = -1)
doppler = pygame.mixer.Sound("material/music/doppler.mp3")
doppler.set_volume(0.2)
zelda = pygame.mixer.Sound("material/music/zelda.mp3")
demon = pygame.mixer.Sound("material/music/demon.mp3")
demon = pygame.mixer.Sound("material/music/demon.mp3")
demon = pygame.mixer.Sound("material/music/demon.mp3")
never = pygame.mixer.Sound("material/music/never.mp3")
never.set_volume(0.7)

def calc(): # tady nevim, jak programu říct: pokud na oné pozici uvidíš znak, udělej (šlo by to vyřešit přidáním random čísel, že třeba na polozku se "znakem" 11 by se deletovalo, 10 quitla apod.)
    znak = fronta[-1]
    if znak == "o":
        pygame.quit()
        exit()

    elif znak == "d":
        fronta.pop
        fronta.pop

    elif znak == "c":
        for _ in range(len(fronta)):
            fronta.pop

    elif znak == "e": # tady bude problém s ukládáním proměnné i nad jedno použití této funkce (aby to answer přežilo ceký cyklus calc() bez toho, aby se znovu vymazal)
        eval(obrazovka)
        answer = obrazovka
        fronta.pop

        if obrazovka == 2:
            color += 1
        if obrazovka == 1953:    # department eastereggů
            doppler.play()
        if obrazovka == 58008:
            zelda.play()
        if obrazovka == 666:
            demon.play()
        if obrazovka == 1987:
            never.play()
        if obrazovka == 215396891: #solar panel easter egg, čislo 215396891, třeba zpusobem exec(celá dinogame)
            
            dino ="""pygame.init() # nutný příkaz hned na začátku pro správnou inicializaci knihovny
                import random
                class Player(pygame.sprite.Sprite): 
                    def __init__(self):
                        super().__init__()
                        man_1 = pygame.image.load("material/dino/man_1.png")
                        man_2 = pygame.image.load("material/dino/man_2.png")
                        man_3 = pygame.image.load("material/dino/man_3.png")
                        man_4 = pygame.image.load("material/dino/man_4.png")
                        self.walking_images = [man_1, man_2, man_3, man_4]
                        self.walking_index = 0
                        self.jump_sound = pygame.mixer.Sound("material/dino/jump.mp3")
                        self.jump_sound.set_volume(0.2)
                        self.image = self.walking_images[self.walking_index]
                        self.rect = self.image.get_rect(bottomleft=(100,0.75*window_height))
                        self.gravity = 0

                    def player_input(self):
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
                            self.gravity = -20
                            self.jump_sound.play()
                    def apply_gravity(self):
                        self.gravity += 1
                        self.rect.y += self.gravity
                        if self.rect.bottom >= 300:
                            self.rect.bottom = 300

                    def animation_state(self):
                        self.walking_index += 0.1
                        if self.walking_index >= 4:
                            self.walking_index = 0
                        self.image = self.walking_images[int(self.walking_index)]

                    def update(self):
                        self.player_input()
                        self.apply_gravity()
                        self.animation_state()

                    
                class Obstacle(pygame.sprite.Sprite):
                    def __init__(self):
                        super().__init__()
                        self.image = pygame.image.load("material/dino/kaktus.png").convert_alpha()
                        size = random.randint(30,80)
                        self.image = pygame.transform.scale(self.image,(size, size))
                        self.rect = self.image.get_rect(bottomleft = (600, 0.75*window_height))
                        self.speed  = 10
                        
                    def update(self):
                        self.rect.x -= 6
                        self.destroy()
                        
                    def destroy(self):
                        if self.rect.x <= -100: 
                            self.kill()

                def is_collision():
                    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False): # False na konci určuje, zda-li má kolidující obstacle zabít
                        obstacle_group.empty()
                        return False
                    return True

                # herní okno
                window_width = 800
                window_height = 400
                screen = pygame.display.set_mode((window_width, window_height))
                    # dvojice (w,h) v parametru se nazývá *tuple*
                pygame.display.set_caption("Dinosauří hra") # nastavíme do hlavičky okna název hry
                
                icondino = pygame.image.load("material/dino/dinoicon.png")  # Make sure the image is in the same directory
                pygame.display.set_icon(icondino)
                
                clock = pygame.time.Clock() # díky hodinám nastavíme frekvenci obnovování herního okna

                # přidání objektů (tzv. surface) do scény
                sky_surface = pygame.Surface((window_width,0.75*window_height))
                sky_surface.fill("darkslategray1")
                ground_surface = pygame.Surface((window_width,0.25*window_height))
                ground_surface.fill("lightsalmon4")

                # text
                text_font = pygame.font.Font("material/dino/PixelifySans.ttf",100)
                text_surface = text_font.render("GAME OVER!", True, "Black")
                text_rect = text_surface.get_rect(center=(window_width/2, window_height/2))

                score_font = pygame.font.Font("material/dino/PixelifySans.ttf",100) # 100 je velikost písma

                # Groups
                # nepřátelé
                obstacle_group = pygame.sprite.Group()

                # hráč
                player = pygame.sprite.GroupSingle()
                player.add(Player())

                game_active = is_collision()

                counter = 110
                bg_music = pygame.mixer.Sound("material/dino/music.mp3")
                bg_music.play(loops = -1)

                count = 0

                # herní smyčka
                while True:
                    # zjistíme co dělá hráč za akci
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit() # zavřeme herní okno
                            exit() # úplně opustíme herní smyčku, celý program se ukončí
                        if event.type == pygame.KEYDOWN:
                            if game_active == False:
                                game_active=True
                                bg_music.play()

                    if game_active:
                        # pozadí
                        screen.blit(sky_surface,(0,0)) # položíme sky_surface na souřadnice [0,0]
                        screen.blit(ground_surface,(0,0.75*window_height)) # položíme ground_surface na souřadnice [0,300] (pod oblohu)

                        if counter > 120:
                            counter = 0
                            obstacle_group.add(Obstacle())
                            
                        else:
                            counter += 1

                        # nepřítel
                        obstacle_group.draw(screen)
                        obstacle_group.update()

                        # hráč
                        player.draw(screen)
                        player.update()
                        
                        count += 1
                        score_surface = text_font.render(f"Skore: {count // 60}", True, "Black") # text, anti-aliasing, černá barva písma
                        score_rect = text_surface.get_rect(center=(window_width/2, window_height/2)) # kam se to má vykreslit
                        screen.blit(score_surface, score_rect)
                        
                        game_active = is_collision()

                    else:
                        pygame.draw.rect(screen, (255,0,0), pygame.Rect(window_width*0.15, window_height*0.25, window_width*0.7, window_height*0.5))
                        count = 0
                        screen.blit(text_surface, text_rect)
                        bg_music.stop()

                    pygame.display.update() # updatujeme vykreslené okno
                    clock.tick(60)"""
            exec(dino)

    elif znak == "a":
        fronta.append(answer)
        fronta.pop

    obrazovka = "".join(fronta)
    print(obrazovka)

names = ["1b.png", "2b.png", "3b.png", "4b.png", "5b.png", "6b.png", "7b.png", "8b.png", "9b.png", "10b.png", 
        "11b.png", "12b.png", "13b.png", "14b.png", "15b.png", "16b.png", "17b.png", "18b.png", "19b.png", "20b.png", 
        "21b.png", "22b.png", "23b.png", "24b.png", "25b.png"]
functions = ["**(1/2)", "**2", " ", "o", " ", "7", "8", "9", "d", "c", 
             "4", "5", "6", "*", "/", "1", "2", "3", "+", "-", 
             "0", "00", " ", "a", "e"]

# o = off, d = delete, c = all clear, a = answer, e = execute (=)

for i in range (0, 24):
        buttons_surface = pygame.image.load(f"material/buttons/{names[i]}")
x = 32
y = 308
buttons_group = pygame.sprite.Group()
mouse = pygame.mouse.get_pos()

def is_collision():
    if pygame.sprite.spritecollide(mouse, buttons_group, False):
        fronta.append(functions[names.index(buttons_group)])
        calc()
# zde je problém, který se vyřeší poté, co se inteligentně načtou všechny buttons
# jak zjistim, se kterým rect to koliduje, abych mohl do fronty appendnout adekvátní znak

window_width = 500
window_height = 600

calculator_surface = pygame.image.load("material/protofin_25_05_25.png")
calculator_surface = pygame.transform.scale(calculator_surface, (window_width, window_height))

screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

while True:

    # zjistíme co dělá hráč za akci
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # zavřeme herní okno
            exit() # úplně opustíme herní smyčku, celý program se ukončí
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_collision()
            
    screen.blit(calculator_surface,(0,0)) # položíme pozadí na souřadnice [0,0]

    for i in range (0, 24):
            for l in range(5):
                for j in range(5):
                    buttons_surface.blit(names[i], (x,y))
                x += 88
            x == 32
            y += 56
    
    pygame.display.update() # updatujeme vykreslené okno
    clock.tick(5) # herní smyčka proběhne maximálně 5x za sekundu

# urgent, displej irl funkční, ukazuje to co je potřeba

# TODO list
#   vytvorit group tlačítek
#   rozmyšlení animace tlačítek
#   vyresit ukazatel postupu
#   https://www.pygame.org/docs/py-modindex.html