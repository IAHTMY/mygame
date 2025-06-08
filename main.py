import pygame # klíčová knihovna umožňující vytvářet jednoduše nejen hry
pygame.init() # nutný příkaz hned na začátku pro správnou inicializaci knihovny

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

fronta = []

def calc(): # tady nevim, jak programu říct: pokud na oné pozici uvidíš znak, udělej (šlo by to vyřešit přidáním random čísel, že třeba na polozku se "znakem" 11 by se deletovalo, 10 quitla apod.)
    znak = fronta[-1]
    if znak == o:
        pygame.quit()
        exit()

    elif znak == d:
        fronta.pop
        fronta.pop

    elif znak == c:
        for _ in len(fronta):
            fronta.pop

    elif znak == e: # tady bude problém s ukládáním proměnné i nad jedno použití této funkce (aby to answer přežilo ceký cyklus calc() bez toho, aby se znovu vymazal)
        eval(obrazovka)
        answer == obrazovka
        fronta.pop
# musím answer před použitím clac() nadefinovat, nemůžu jí ale přiřadit číslo -> po spuštění by se hned mohlo použít i bez předchozího výpočtu (například 0)
# musím zavést globální proměnnou, která se bude moci menit skrz používání programu a zároveň na začátku nebude mít hodnotu (nebude definovaná)
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
            pass

    elif znak == a:
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
#   připravit hudbu
#   rozmyšlení animace tlačítek
#   vyresit ukazatel postupu

#   parapetry tlačítek 39*23 (stará verze někdy i 41*23)
#   užitečné
#   https://www.pygame.org/docs/py-modindex.html