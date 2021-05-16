
from pygame.sprite import Sprite, collide_rect
from pygame import Surface, mixer
import pyganim # импортируем весь каталог с анимациями

# настройки звука
mixer.pre_init(44100, -16, 1, 512)
mixer.init()

MOVE_SPEED = 7 # скорость (изменение по координате x)
JUMP_POWER = 10 # сила прыжка (изменение по координате y)

GRAVITY = 0.4 # гравитация (с какой скоростью герой падает)
COLOR = (154, 154, 154) # цвет героя (несмотря на текстуры)

ANIMATION_DELAY = 0.1 # время задержки
# изображение героя
ANIMATION_STAY = [('images/hero/hero.png', ANIMATION_DELAY)]
# изображения анимации ходьбы вправо
ANIMATION_RIGHT = [('images/hero/hero_right1.png'),
                   ('images/hero/hero_right2.png'),
                   ('images/hero/hero_right3.png'),
                   ('images/hero/hero_right4.png'),
                   ('images/hero/hero_right5.png'),
                   ('images/hero/hero_right6.png'),
                   ('images/hero/hero_right7.png'),
                   ('images/hero/hero_right8.png'),
                   ('images/hero/hero_right9.png'),
                   ('images/hero/hero_right10.png')]
# изображения анимации ходьбы влево
ANIMATION_LEFT = [('images/hero/hero_left1.png'),
                  ('images/hero/hero_left2.png'),
                  ('images/hero/hero_left3.png'),
                  ('images/hero/hero_left4.png'),
                  ('images/hero/hero_left5.png'),
                  ('images/hero/hero_left6.png'),
                  ('images/hero/hero_left7.png'),
                  ('images/hero/hero_left8.png'),
                  ('images/hero/hero_left9.png'),
                  ('images/hero/hero_left10.png')]
# изображения анимации прыжка (обычного и при нажатии вправо)
ANIMATION_UP = [('images/hero/hero_up1.png'),
                ('images/hero/hero_up2.png'),
                ('images/hero/hero_up3.png'),
                ('images/hero/hero_up4.png'),
                ('images/hero/hero_up5.png'),
                ('images/hero/hero_up6.png'),
                ('images/hero/hero_up7.png'),
                ('images/hero/hero_up8.png'),
                ('images/hero/hero_up9.png'),
                ('images/hero/hero_up10.png'),
                ('images/hero/hero_up11.png'),
                ('images/hero/hero_up12.png')]
# изображения анимации прыжка (при нажатии влево)
ANIMATION_UPLEFT = [('images/hero/hero_up_left1.png'),
                ('images/hero/hero_up_left2.png'),
                ('images/hero/hero_up_left3.png'),
                ('images/hero/hero_up_left4.png'),
                ('images/hero/hero_up_left5.png'),
                ('images/hero/hero_up_left6.png'),
                ('images/hero/hero_up_left7.png'),
                ('images/hero/hero_up_left8.png'),
                ('images/hero/hero_up_left9.png'),
                ('images/hero/hero_up_left10.png'),
                ('images/hero/hero_up_left11.png'),
                ('images/hero/hero_up_left12.png')]

# создание героя
class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((38, 38)) # размер героя (в пикселях)
        self.xvel = 0 # изначальные координаты героя
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False # изначально не на земле

        def make_boltAnim(anim_list, delay): # функция с помощью которой анимации будут по очереди производиться
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY) # анимация это свойство объекта
        self.boltAnimStay.play()

        self.boltAnimRight = make_boltAnim(ANIMATION_RIGHT, ANIMATION_DELAY) # анимация это свойство объекта
        self.boltAnimRight.play()
        self.walk_sound = mixer.Sound('sounds/walk.ogg') # добавляем звук ходьбы

        self.boltAnimLeft = make_boltAnim(ANIMATION_LEFT, ANIMATION_DELAY) # анимация это свойство объекта
        self.boltAnimLeft.play()
        self.walk_sound = mixer.Sound('sounds/walk.ogg') # добавляем звук ходьбы

        self.boltAnimUp = make_boltAnim(ANIMATION_UP, ANIMATION_DELAY) # анимация это свойство объекта
        self.boltAnimUp.play()
        self.jump_sound = mixer.Sound('sounds/jump.ogg') # добавляем звук прыжка

        self.boltAnimUpLeft = make_boltAnim(ANIMATION_UPLEFT, ANIMATION_DELAY) # анимация это свойство объекта
        self.boltAnimUpLeft.play()
        self.jump_sound = mixer.Sound('sounds/jump.ogg') # добавляем звук прыжка

    # изменения героя при нажатии клавиш
    def update(self, left, right, up, platforms):
        if up: # если нажато вверх
            if self.onGround: # если герой на земле
                self.yvel = -JUMP_POWER # по координате y отнимаем значения и получем прыжок
                self.jump_sound.play() # воспроизводим звук
            self.image.fill(COLOR)
            self.boltAnimUp.blit(self.image, (0, 0)) # играется анимация прыжка

        if not self.onGround: # если не на земле
            self.yvel += GRAVITY # ничего не произойдет (можем прыгнуть только на земле)

        if left: # если нажато влево
            self.xvel = -MOVE_SPEED # по координате x отнимаем значения и движемся влево
            self.walk_sound.play() # воспроизводим звук
            self.image.fill(COLOR)
            if up:  # для прыжка влево есть отдельная анимация
                self.boltAnimUpLeft.blit(self.image, (0, 0)) # анимация при нажатии вверх и влево
            else:
                self.boltAnimLeft.blit(self.image, (0, 0)) # если не нажато вверх то просто он идет по земле
        if right: # если нажато вправо
            self.xvel = MOVE_SPEED # по координате x прибавляем значения и движемся право
            self.walk_sound.play() # воспроизводим звук
            self.image.fill(COLOR)
            if up: # при прыжке и направо
                self.boltAnimUp.blit(self.image, (0, 0)) # анимация прыжка направо
            else:
                self.boltAnimRight.blit(self.image, (0, 0)) # если не нажато вверх то просто он идет по земле
        if not(left or right): # если не двигается
            self.xvel = 0 # не меняесть координата x
            if not up: # если еще и не прыгает то воспроизводит изобржение героя
                self.image.fill(COLOR)
                self.boltAnimStay.blit(self.image, (0, 0)) # изображение героя


        self.onGround = False
        self.rect.x += self.xvel # вызываем проверку столкновений по x
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel # вызываем проверку столкновений по y
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms): # проверка столкновений
        for pl in platforms: # pl это блок кирпича
            if collide_rect(self, pl): # если герой столкнулся с блоком кирпича
                if xvel > 0: # не проходит насквозь ее слева
                    self.rect.right = pl.rect.left
                if xvel < 0: # не походит насквозь ее справа
                    self.rect.left = pl.rect.right
                if yvel > 0: # стоит на платформе
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0: # снизу платформы. бьется об нее
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0 # обнуление скорости не у не дает герою прилипнуть снизу платформы