import random
from math import *

import pygame

pygame.init()
W = 1400
H = 447
WHITE = (255, 255, 255)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
NUM_OF_MAN = 21
NUM_OF_BIRD = 13

PATH_TO_BG = 'new_sprites/bg.png'
H_GROUND = 335

functions = [
    lambda x: 0.1 * (0.5 * x) ** 2,
    lambda x: 100 * cos(0.01 * x) + 180,
    lambda x: 100 * sin(0.02 * x) + 180,
    lambda x: sqrt(300 * x),
    lambda x: sqrt(350 * x),
    lambda x: 50 * log(x)
]


class Window(object):
    def __init__(self):
        self.sc = pygame.display.set_mode((W, H))
        self.back_surf = pygame.image.load(PATH_TO_BG).convert()
        self.back_rect = self.back_surf.get_rect()
        self.sc.blit(self.back_surf, self.back_rect)


master = Window()


class Entity(pygame.sprite.Sprite):
    def __init__(self, filename: str, x_start: int, y_start: int, pos: int, resize=3):
        super().__init__()
        self.filename = filename
        self.image = pygame.image.load(filename).convert_alpha()
        self.resize = resize
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // resize,
                                                         self.image.get_height() // resize))

        if pos == 0:
            self.rect = self.image.get_rect(topleft=(x_start, y_start))
        elif pos == 1:
            self.rect = self.image.get_rect(topright=(x_start, y_start))
        elif pos == 2:
            self.rect = self.image.get_rect(bottomright=(x_start, y_start))
        elif pos == 3:
            self.rect = self.image.get_rect(bottomleft=(x_start, y_start))
        elif pos == 4:
            self.rect = self.image.get_rect(center=(x_start, y_start))

    def reDraw(self, filename, direction=RIGHT):
        self.filename = filename
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.resize,
                                                         self.image.get_height() // self.resize))
        if direction == LEFT:
            self.image = pygame.transform.flip(self.image, 1, 0)

    def ID(self):
        return int(self.filename.split('/')[-1][0:-4])


class Bird(Entity):
    def __init__(self, x: int, y: int, pos: int, func):
        self.filename = 'new_sprites/bird/0.png'
        super().__init__(self.filename, x, y, pos, 2)

        self.func = func
        self.x_0 = x
        self.y_0 = y
        self.speed = 3
        if W // 2 - 150 < x < W // 2 + 150:
            x = 15
        if x < W // 2 - 150:
            self.direct = RIGHT
        else:
            self.direct = LEFT

    def update(self):
        global functions
        if self.direct == RIGHT:
            self.rect.x += 3
            self.rect.y = self.func(abs(self.rect.x - self.x_0))
        elif self.direct == LEFT:
            self.rect.x -= 2
            self.rect.y = self.func(abs(self.rect.x - self.x_0))
        if not (0 <= self.rect.x <= W and 0 <= self.rect.y <= H_GROUND):
            self.x_0 = self.rect.x = random.randint(5, W - 5)
            self.y_0 = self.rect.y = 5
            self.speed = random.randint(2, 4)
            self.func = functions[random.randint(0, len(functions) - 1)]

        self.reDraw(f'new_sprites/bird/{str((self.ID() + 1) % NUM_OF_BIRD)}.png', self.direct)


class Man(Entity):
    def __init__(self, x: int, y: int, pos):
        self.filename = 'new_sprites/man/57.png'
        super().__init__(self.filename, x, y, pos)
        self.motion = STOP
        self.speed = 5

    def update(self, direct: str):
        if direct == LEFT and self.rect.x > 15:
            self.rect.x -= self.speed
            self.reDraw(f'new_sprites/man/{str((self.ID() + 1) % NUM_OF_MAN)}.png', LEFT)

        elif direct == RIGHT and self.rect.x < W - 50:
            self.rect.x += self.speed
            self.reDraw(f'new_sprites/man/{str((self.ID() + 1) % NUM_OF_MAN)}.png', RIGHT)

        elif direct == STOP:
            self.reDraw(f'new_sprites/man/57.png', self.motion)

        self.motion = direct


myMan = Man(random.randint(1, W), H_GROUND, 4)
birds = pygame.sprite.Group(
    Bird(random.randint(10, W - 10), 5, 0, functions[random.randint(0, len(functions) - 1)]),
    Bird(random.randint(10, W - 10), 5, 0, functions[random.randint(0, len(functions) - 1)]),
    Bird(random.randint(10, W - 10), 5, 0, functions[random.randint(0, len(functions) - 1)]),
    Bird(random.randint(10, W - 10), 5, 0, functions[random.randint(0, len(functions) - 1)]),
    Bird(random.randint(10, W - 10), 5, 0, functions[random.randint(0, len(functions) - 1)]),
)

pygame.display.update()

while 1:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                myMan.update(LEFT)
            elif event.key == pygame.K_RIGHT:
                myMan.update(RIGHT)
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                myMan.update(STOP)

    if myMan.motion == LEFT:
        myMan.update(LEFT)
    elif myMan.motion == RIGHT:
        myMan.update(RIGHT)

    master.sc.blit(master.back_surf, master.back_rect)
    master.sc.blit(myMan.image, myMan.rect)
    birds.draw(master.sc)

    pygame.display.update()
    pygame.time.delay(40)

    birds.update()
