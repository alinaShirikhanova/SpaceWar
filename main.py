import pygame as pg

from util import load_image

pg.init()

WIDTH, HEIGHT = (900, 500)
screen = pg.display.set_mode((WIDTH, HEIGHT))

PL_WIDTH, PL_HEIGHT = 50, 50

# Загрузка фона
bg = load_image('space.png')
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))

# Загрузка изображения первого игрока
player1 = load_image('player1.png')
player1 = pg.transform.scale(player1, (PL_WIDTH, PL_HEIGHT))

# Загрузка изображения второго игрока
player2 = load_image('player2.png')
player2 = pg.transform.scale(player2, (PL_WIDTH, PL_HEIGHT))




running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    screen.blit(player1, (WIDTH // 4, HEIGHT // 2))
    screen.blit(player2, (WIDTH - WIDTH // 4, HEIGHT // 2))



    pg.display.update()


