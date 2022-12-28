import pygame as pg
import sys, os
from pygame.locals import *
from pygame import mixer

pg.init()
mixer.init()
screen = pg.display.set_mode((500,500))
simWindow = pg.Rect(50, 50, 400, 400)

#music
mixer.init()
music = pg.mixer.music.load("C:/Users/hello/PycharmProjects/pythonProject/win-sfx-38507.ogg")
pg.mixer.music.play()

#colors
black = (0, 0, 0)

screen.fill(black)
pg.Surface.fill(screen, black, simWindow)

#text
win_text = pg.image.load("C:/Users/hello/PycharmProjects/pythonProject/text-1672257287630.png")
win_text = pg.transform.scale(win_text, (100, 100))


thanku_text = pg.image.load("C:/Users/hello/PycharmProjects/pythonProject/text-1672257316986.png")
thanku_text = pg.transform.scale(thanku_text, (200, 150))


running = True

while running:
    screen.blit(win_text, (200, 50))
    screen.blit(thanku_text,(100,300))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()
