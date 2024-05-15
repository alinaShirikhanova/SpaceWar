import pygame as pg
import os
import sys


def load_image(name, color_key=None):
    fullname = os.path.join('data/images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не существует')
        sys.exit()
    image = pg.image.load(fullname)
    if color_key is not None:
        image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image.convert_alpha()
    return image