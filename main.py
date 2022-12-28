import pygame as pg
import sys, os
from pygame.locals import *
from pygame import mixer

pg.init()
mixer.init()
screen = pg.display.set_mode((500,500))
bg = pg.image.load("C:/Users/hello/PycharmProjects/pythonProject/Pixel_art_grass_image.png")

#music
mixer.init()
music = pg.mixer.music.load("C:/Users/hello/PycharmProjects/pythonProject/2021-08-16_-_8_Bit_Adventure_-_www.FesliyanStudios.com.ogg")
pg.mixer.music.play()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#fps
FPS = pg.time.Clock()

simWindow = pg.Rect(50, 50, 400, 400)

#background
screen.fill(white)
pg.Surface.fill(screen, white, simWindow)

#player
player = pg.image.load("C:/Users/hello/PycharmProjects/pythonProject/YGpOh.png")
default_player_pos_x = 0
default_player_pos_y = 0

#player resize
player_x_size = 150
player_y_size = 150
player = pg.transform.scale(player, (player_x_size,player_y_size))

#coin
coin = pg.image.load("C:/Users/hello/PycharmProjects/pythonProject/download-removebg-preview.png")
coin_x, coin_y = 200, 300
default_coin_pos = (coin_x,coin_y)
#coin resize
coin_x_size = 50
coin_y_size = 50
coin = pg.transform.scale(coin, (coin_x_size, coin_y_size))









running = True


while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                default_player_pos_x -= 1
            if event.key == pg.K_RIGHT:
                default_player_pos_x += 1
            if event.key == pg.K_UP:
                default_player_pos_y -= 1
            if event.key == pg.K_DOWN:
                default_player_pos_y += 1
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                default_player_pos_x -= 1
            if keys[pg.K_RIGHT]:
                default_player_pos_x += 1
            if keys[pg.K_UP]:
                default_player_pos_y -= 1
            if keys[pg.K_DOWN]:
                default_player_pos_y += 1
        if event.type == pg.QUIT:
             running = False
    pg.display.flip()
    FPS.tick(120)
    screen.blit(bg, (0, 0))
    screen.blit(player,(default_player_pos_x,default_player_pos_y))
    screen.blit(coin,default_coin_pos)
    if (default_player_pos_x >= coin_x-50 and default_player_pos_x <= coin_x+50 ) or (default_player_pos_y >= coin_y-40 and default_player_pos_y <= coin_y+50):
        import win
        pg.quit()
        exec(open('win.py').read())
    pg.display.update()



