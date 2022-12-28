import pygame as pg
import sys, os
from pygame.locals import *
from pygame import mixer

#initializes the game and music
pg.init()
mixer.init()
screen = pg.display.set_mode((500,500))
simWindow = pg.Rect(50, 50, 400, 400)



#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

#fills screen
screen.fill(black)
pg.Surface.fill(screen, black, simWindow)
#text
text = pg.image.load("C:/Users/hello/PycharmProjects/pythonProject/text-1672174617745.png")
text = pg.transform.scale(text, (300, 200))
screen.blit(text, (50, 50))

#starts timing
start_ticks=pg.time.get_ticks() #starter tick

#runs the screen
running = True

while running:
    screen.blit(text, (50, 50))
    seconds = (pg.time.get_ticks() - start_ticks) / 1000
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if seconds == 3:
        import main
        pg.quit()
        exec(open('main.py').read())
    pg.display.update()





