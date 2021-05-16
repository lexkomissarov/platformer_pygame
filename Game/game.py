
import pygame   # импортируем библиотеку pygame
from player import Player  # с помощью from можно импортировать отдельные части из других каталогов
from Platforms import Platform  # этот метод позволяет не нагружать оперативную память
from Platforms import Meat
from Platforms import Finish
from Platforms import goR
from Platforms import goD
from Platforms import PIPE
from Platforms import WOOD
from Platforms import BOX



SIZE = (640, 480)  # разрешение экрана (переменная)

# создаём окно
window = pygame.display.set_mode(SIZE)
# создаём рабочую поверхность (игровой экран)
screen = pygame.Surface(SIZE)
# название окна
pygame.display.set_caption("Приключения динозаврика Игната")
# иконка окна
icon = pygame.image.load("icon/icon.png")
pygame.display.set_icon(icon)

# создание героя
hero = Player(80, 80)  # в скобках его координаты в начале по (x, y)
left = right = up = False  # стоять по умолчанию

# создание уровня (шаблон)(далее разъяснение символов)
level = [
       "--------->------------------------",
       "-   -                            V",
       "-   -    -   -   W  W   W   ---- -",
       "-WW -   W-  W-  WW WW  WW  --  - -",
       "-   -    -W  -                 - -",
       "- WW-    -   -                 - -",
       "-   -   W-  W-                 - -",
       "-WW -    -   ----------------- - -",
       "-   -    -W                    - -",
       "- WW-   W-                     - -",
       "-   P    -  B                  - -",
       "-        -  B                  - -",
       "-------------------------------- -",
       "-  P   P   P   P   P   P   P   P -",
       "V    B   B   B   B   B   B   B   -",
       "-  -------------------------------",
       "-                                -",
       ">                                V",
       "- W  WW  WW  WW  WW  WW  WW   B  -",
       "-                             B  -",
       "-W                            BFF-",
       "-                             B  -",
       "-                             BMM-",
       "----------------------------------"]

# добавляем героя в игру
sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platforms = [] # то, во что мы будем врезаться или опираться

# обозначения сисволов на шаблоне (делаем уровень из шаблона)
x = 0 # координаты "воображаемого" курсора
y = 0 # он следует по каждому символу
for row in level: # перебираем строки из level
    for col in row: # перебираем символы в строке
        if col == '-': # проверяем символ. если - то
            pl = Platform(x, y) # присваиваем текстуру платформы (кирпич)
            sprite_group.add(pl) # добавляем ее
            platforms.append(pl) # сталкновение
        if col == 'M': # если М
            mt = Meat(x, y) # то присваиваем текстуру мяса
            sprite_group.add(mt) # добавляем ее
            platforms.append(mt) # сталкновение
        if col == 'F': # если F
            fn = Finish(x, y) # то присваиваем текстуру финиша
            sprite_group.add(fn) # добавляем ее | неосязаема
        if col == '>': # если >
            gr = goR(x, y) # присваиваем текстуру стрелки направо
            sprite_group.add(gr) # добавляем ее
            platforms.append(gr) # сталкновение
        if col == 'V': # если V
            gd = goD(x, y) # присваиваем текстуру стрелки вниз
            sprite_group.add(gd) # добавляем ее
            platforms.append(gd) # сталкновение
        if col == 'B': # если B
            box = BOX(x, y) # присваиваем текстуру коробки
            sprite_group.add(box) # добавляем ее
            platforms.append(box) # сталкновение
        if col == 'W': # если W
            wood = WOOD(x, y) # присваиваем текстуру доски
            sprite_group.add(wood) # добавляем ее
            platforms.append(wood) # сталкновение
        if col == 'P': # если P
            pipe = PIPE(x, y) # присваиваем текстуру трубы
            sprite_group.add(pipe) # добавляем ее
            platforms.append(pipe) # сталкновение
        x += 40  # изменение координат
    y += 40 # изсенеие высоты
    x = 0 # обнуляем строку т.к. надо начинать каждую строку с первого символа

# камера
class Camera:
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft) # расстановка объектов по их координатам внутри прямоугольника

    def update(self, target): # вызывает функцию конфигурирования и получаем пустой прямоугольник
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect): # изменение положения камеры
    l = -target_rect.x + SIZE[0]/2
    t = -target_rect.y + SIZE[1]/2
    w, h = camera.width, camera.height
    # не даем заехать за границы карты
    l = min(0, l) # не движемся дальше левой границы
    l = max(-(camera.width-SIZE[0]), l) # не движемся дальше правой границы
    t = max(-(camera.height-SIZE[1]), t) # не движемся дальше нижней границы
    t = min(0, t) # не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)

total_level_width = len(level[0])*40 # ширина уровня = кол-во блоков уровня * ширина 1 блока
total_level_height = len(level)*40 # высота уровня = кол-во строк * ширина 1 блока

camera = Camera(camera_func, total_level_width, total_level_height) # создание объекта камера и придаем значения

# звук
pygame.mixer.pre_init(44100, -16, 1, 512) # параметры (частота/можно сказать константа  /канал/буфер(килобайт))
pygame.mixer.init()
sound = pygame.mixer.Sound('sounds/tema.ogg') # музыка на заднем плане
sound.play(-1) # -1 означает зацикленность

# открываем игровой цикл
done = True
timer = pygame.time.Clock()
while done:
    # блок управления событиями
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        # проверяем нажатие клавиш
        if e.type == pygame.KEYDOWN: # если нажата
            if e.key == pygame.K_LEFT: # проверяем какая
                left = True # и присваиваем истину
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True

        if e.type == pygame.KEYUP: # если не нажата
            if e.key == pygame.K_LEFT: # проверяем какая
                left = False # и присваиваем ложь
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False

    # закрашиваем рабочую поверхность
    screen.fill((154, 154, 154))

    # отображение героя
    hero.update(left, right, up, platforms)
    camera.update(hero) # обновляем камеру по герою
    for e in sprite_group: # отображение всех объектов
        screen.blit(e.image, camera.apply(e))

    # отображаем рабочую поверхность в окне
    window.blit(screen,(0,0))
    # обновляем окно
    pygame.display.flip()
    timer.tick(60) # кадры в секунду