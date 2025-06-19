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
color_set = ["black", "blue", "green", "yellow", "red", "black"]
color_index = 0

text_font = pygame.font.SysFont('arial', 24)
# text_font = pygame.font.Font("material/techfont.ttf",50) # 100 je velikost písma
# text_surface = text_font.render(f"{obrazovka}", True, color) # text, anti-aliasing, černá barva písma
# text_rect = text_surface.get_rect(topleft = (62, 62)) # kam se to má vykreslit

# HUDBA
bg_music = pygame.mixer.Sound("material/music/elevator.mp3")
bg_music.play(loops = -1)
bg_music.set_volume(0.17)
doppler = pygame.mixer.Sound("material/music/doppler.mp3")
doppler.set_volume(0.2)
zelda = pygame.mixer.Sound("material/music/zelda.mp3")
demon = pygame.mixer.Sound("material/music/demon.mp3")
never = pygame.mixer.Sound("material/music/never.mp3")
never.set_volume(0.7)
bonk = pygame.mixer.Sound("material/music/bonk.mp3")
lacrimosa = pygame.mixer.Sound("material/music/lacrimosa.mp3")

# REAKCE NA INPUTY
def calc(): 
    global obrazovka
    global answer
    global color_index

    try:
        znak = fronta[-1]

        if len(fronta) == 2 and fronta[-2] == "Error":
            fronta.pop(-2)

        elif len(fronta) >= 15:
            obrazovka = ''.join([obrazovka[i] for i in range(len(obrazovka)) if i < 20])
            while len(fronta) >= 14:
                fronta.pop()

        elif znak == "o":
            fronta.pop()
            pygame.quit()
            exit()

        elif znak == "b":
            fronta.pop()
            bonk.play()

        elif znak == "d":
            if len(fronta) == 1:
                fronta.pop()
            else:
                fronta.pop()
                fronta.pop()

        elif znak == "c":
            for _ in range(len(fronta)):
                fronta.pop()

        elif znak == "a":
            fronta.pop()
            fronta.append(answer)

        elif znak == "e":
            fronta.pop()

            """
            eval("answer = " + obrazovka) 
            help = 0
            number = [[]]
            front = []
            for i in obrazovka:
                if i.isnumber():
                    number[help].append(int(i))
                else:
                    number.append()
                    help += 1
                    front.append(i)
            for i in number:
                if front[0] == "*":
            """
            if len(fronta) != 0:
                obrazovka = "".join(fronta)
                print(obrazovka)
                print(eval(obrazovka))
                obrazovka = eval((obrazovka))
                
        # department eastereggů
            if obrazovka == 2:
                color_index += 1
            if obrazovka == 1953:    
                doppler.play()
            if obrazovka == 7:
                zelda.play()
            if obrazovka == 666:
                demon.play()
            if obrazovka == 1987:
                never.play()
            if obrazovka == 215396891: #solar panel easter egg, čislo 215396891, třeba zpusobem exec(celá dinogame)
                pygame.mixer.pause()
                lacrimosa.play()
                print("Jsem rád, že jste to zrovna vy, kdo jste objevil tento easteregg. Zdá se, že jste tímto rozbili celý program. \n Prosím, zatímco budu tento kód opravovat, vychutnejte si tuto píseň od Mozarta - Lacrimosa")
                pygame.time.delay(188000)
                pygame.mixer.unpause()
    except:
        for _ in range(len(fronta)):
                fronta.pop()
        fronta.append("Error")
    finally:
        obrazovka = "".join(fronta)

names = ["1b.png", "2b.png", "3b.png", "4b.png", "5b.png", "6b.png", "7b.png", "8b.png", "9b.png", "10b.png", 
        "11b.png", "12b.png", "13b.png", "14b.png", "15b.png", "16b.png", "17b.png", "18b.png", "19b.png", "20b.png", 
        "21b.png", "22b.png", "23b.png", "24b.png", "25b.png"]
functions = ["**(1/2)", "**2", "(", ")", "o", "7", "8", "9", "d", "c", 
             "4", "5", "6", "*", "/", "1", "2", "3", "+", "-", 
             "0", "00", "b", "a", "e"]

class Button(pygame.sprite.Sprite): 
    def __init__(self, index, pos_x, pos_y):
        super().__init__()
        self.image=pygame.image.load(f"material/buttons/{names[index]}")
        self.rect=self.image.get_rect(topleft=(pos_x,pos_y))

        self.index = index 

        # print("button init", pos_x, pos_y)
# o = off, d = delete, c = all clear, a = answer, e = execute (=)
x = 32
y = 308
buttons_group = pygame.sprite.Group()
id = 0
for _ in range(5):
    for _ in range(5):
        buttons_group.add(Button(id, x, y))
        id += 1
        x += 88
    x = 32
    y += 56
    
def is_collision(position):
    for button in buttons_group.sprites():
        # if pygame.sprite.spritecollide(position, button, False):
        if button.rect.collidepoint(position):
            fronta.append(functions[button.index])
            calc()

window_width = 500
window_height = 600

calculator_surface = pygame.image.load("material/protofin.png")
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
            is_collision(event.pos)
    
    screen.fill("black")
    screen.blit(calculator_surface,(0,0)) # položíme pozadí na souřadnice [0,0]

    buttons_group.draw(screen)
    buttons_group.update()

    # TEXT na kalkulacke
    if color_index >= len(color_set):
        color_index = 0
    color = color_set[color_index]
    # print("text:", obrazovka)
    calculator_text_surface = text_font.render(f"{obrazovka}", True, color) # tady je potřeba přidat tu proměnnou barvu
    screen.blit(calculator_text_surface, (62, 62))
    
    pygame.display.update()
    clock.tick(5)

# TODO list
# vytvořit scénář, kdy je výsledek moc dlouhý/zadává se moc věcí do calc
# dle https://pythonbasics.org/try-except/