
from pygame.sprite import Sprite
from pygame.image import load

# добавляем платформу (блок кирпича)
class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platform/platform.png') # текстура
        self.rect = self.image.get_rect() # накладываем текстуру
        self.rect.x = x # координаты платформы равны тем которые ему присвоят
        self.rect.y = y

# добавляем мясо
class Meat(Sprite): # все аналогично кирпичу
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/meat/meat.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# добавляем финиш
class Finish(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platform/finish.png') # текстура
        self.rect = self.image.get_rect() # накладываем текстуру
        self.rect.x = x # координаты платформы равны тем которые ему присвоят
        self.rect.y = y

# добавляем стрелки
class goR(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platform/goR.png') # текстура
        self.rect = self.image.get_rect() # накладываем текстуру
        self.rect.x = x # координаты платформы равны тем которые ему присвоят
        self.rect.y = y

# добавляем стрелки
class goD(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platform/goD.png') # текстура
        self.rect = self.image.get_rect() # накладываем текстуру
        self.rect.x = x # координаты платформы равны тем которые ему присвоят
        self.rect.y = y

# добавляем коробки
class BOX(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platform/box.png') # текстура
        self.rect = self.image.get_rect() # накладываем текстуру
        self.rect.x = x # координаты платформы равны тем которые ему присвоят
        self.rect.y = y

# добавляем трубу
class PIPE(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platform/pipe.png') # текстура
        self.rect = self.image.get_rect() # накладываем текстуру
        self.rect.x = x # координаты платформы равны тем которые ему присвоят
        self.rect.y = y

# добавляем доски
class WOOD(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/platform/wood.png') # текстура
        self.rect = self.image.get_rect() # накладываем текстуру
        self.rect.x = x # координаты платформы равны тем которые ему присвоят
        self.rect.y = y