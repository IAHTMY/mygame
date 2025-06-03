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
class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
#       self.image = pygame.image.load("kaktus.png").convert_alpha()
#       self.image = pygame.transform.scale(self.image,(size, size))
#       self.rect = self.image.get_rect(bottomleft = (600, 0.75*window_height))
#       but_1 = pygame.image.load("but_1.png")
#       
#       self.walking_images = [man_1, man_2, man_3, man_4]
#       self.walking_index = 0

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
def calc():
    znak = fronta[-1]
    if znak == o:
        pygame.quit() # zavřeme herní okno
        exit() # úplně opustíme herní smyčku, celý program se ukončí
    elif znak == d:
        fronta.pop
        fronta.pop
    elif znak == c:
        for i in len(fronta):
            fronta.pop
    elif znak == e:
        vysledek = ()
        for i in len(fronta):
            vysledek.append(fronta[i]) # Tady se mu nelíbí, že nepracuju s listem. kdybych mu tam dal integer, fungovalo by to do té doby, dokud bych tam neměl znaménko +-/*...
        print(vysledek)
        answer == vysledek
        # přepsání listu do (), pak se to vyprintne a na tuto hodnotu se promění i hodnota answer
    elif znak == a:
        fronta.append(answer)
    

    if vysledek == 1953:    # department eastereggů
        doppler.play()
    if vysledek == 58008:
        zelda.play()
    if vysledek == 666:
        demon.play()

    if vysledek == 215396891: #solar panel easter egg, čislo 215396891
        never.play()

names = ["1b.png", "2b.png", "3b.png", "4b.png", "5b.png", "6b.png", "7b.png", "8b.png", "9b.png", "10b.png", 
        "11b.png", "12b.png", "13b.png", "14b.png", "15b.png", "16b.png", "17b.png", "18b.png", "19b.png", "20b.png", 
        "21b.png", "22b.png", "23b.png", "24b.png", "25b.png"]
functions = ["**(1/2)", "**2", " ", "o", " ", "7", "8", "9", "d", "c", 
             "4", "5", "6", "*", "/", "1", "2", "3", "+", "-", 
             "0", "00", " ", "a", "e"]
# o = off, d = delete, c = all clear, a = answer, e = execute (=)

for i in range (0, 24):
        buttons_surface = pygame.image.load(f"material/buttons/{names[i]}")
x = 40
y = 250
buttons_group = pygame.sprite.Group()
def is_collision():
    if pygame.sprite.spritecollide(mouse, buttons_group, False): # False na konci určuje, zda-li má kolidující obstacle zabít
        fronta.append(functions[names.index(buttons_group)])
        calc()

window_width = 500
window_height = 600

calculator_surface = pygame.image.load("material/protofin_25_05_25.png")
calculator_surface = pygame.transform.scale(calculator_surface, (500,600))
"""
text_font = pygame.font.Font("PixelifySans.ttf",100) # 100 je velikost písma
text_surface = text_font.render("GAME OVER!", True, "Black") # text, anti-aliasing, černá barva písma
text_rect = text_surface.get_rect(20, 20) # kam se to má vykreslit
"""
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

print(eval(""))

exec("""
a = 7
b = 8
print("vysledek: ", a*b)
""")

while True:

    # zjistíme co dělá hráč za akci
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # zavřeme herní okno
            exit() # úplně opustíme herní smyčku, celý program se ukončí
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_collision()
            
    screen.blit(calculator_surface,(0,0)) # položíme pozadí na souřadnice [0,0]
    for j in range (1, 5):
        for i in range (0, 24):
            buttons_surface.blit(names[i], (x,y))
        x += 84
    x == 40
    y += 52
    buttons_surface.blit()
    mouse = pygame.mouse.get_pos()
    print(mouse)
    

# pokud klkiknu na tlačítko, ať se appendne indexem daný znak a pak se spustí funkce kalkulačky, která bude kontrolovat poslední část fronty


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