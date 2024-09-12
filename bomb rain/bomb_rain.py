import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

pygame.init()

pygame.display.set_caption('BOMB RAIN')
fps = pygame.time.Clock()
tela = pygame.display.set_mode((640, 480))
cenario = pygame.image.load('cenario.png').convert()
sprite_explosion = pygame.image.load('explosion.png').convert_alpha()
sprite_personagem = pygame.image.load('personagem.png').convert_alpha()
spr = sprite_personagem.get_rect(topleft=(300, 350))
sprite_bomb = pygame.image.load('bomb.png').convert_alpha()
sbrs = []
for i in range(0, 6):
    sbrs.append(sprite_bomb.get_rect(topleft=(randint(40, 600), -20)))
x_sprite_bomb = 0
y_sprite_bomb = 0
x_sprite_personagem = 0
y_sprite_personagem = 0
morte = False
cont = 1

while True:

    tela.blit(cenario, (0, 0))
    fps.tick(30)
    
    if (morte):
        fps.tick(10)
        if (cont == 1):
            x_sprite_explosion = 0
            while x_sprite_explosion <= 20:
                x_sprite_explosion = x_sprite_explosion + 0.001
                tela.blit(sprite_explosion, (bomb_rects[j].x, bomb_rects[j].y), (int(x_sprite_explosion)*32, 0, 32, 32)) 
        if (x_sprite_personagem >= 5):
            sleep(5)
            pygame.quit()
            exit()
        x_sprite_personagem = x_sprite_personagem + 0.15
        tela.blit(sprite_personagem, spr, (int(x_sprite_personagem)*96, 192, 96, 96))
        cont = cont + 1
    else:
        bomb_rects = []

        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
        
        tela.blit(sprite_personagem, spr, (int(x_sprite_personagem)*96, y_sprite_personagem, 96, 96))

        if (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]):
            x_sprite_personagem = x_sprite_personagem + 0.25
            y_sprite_personagem = 96
            spr.x = spr.x - 7
        elif (pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]):
            x_sprite_personagem = x_sprite_personagem + 0.25
            y_sprite_personagem = 0
            spr.x = spr.x + 7
        else:
            x_sprite_personagem = x_sprite_personagem + 0.2
            y_sprite_personagem = 288
        
        if (y_sprite_personagem == 288):
            if (x_sprite_personagem >= 3):
                x_sprite_personagem = 0
        else:
            if (x_sprite_personagem >= 5):
                x_sprite_personagem = 0

        for i in range(0, 6):
            tela.blit(sprite_bomb, sbrs[i], (int(x_sprite_bomb)*32, y_sprite_bomb, 32, 32))
            bomb_rects.append(sbrs[i])

        x_sprite_bomb = x_sprite_bomb + 0.25
        if (x_sprite_bomb == 2):
            x_sprite_bomb = 0

        for j in range(len(bomb_rects)):
            if (bomb_rects[j].y >= spr.y and bomb_rects[j].x >= spr.x and bomb_rects[j].x <= (spr.x + 96)):
                bomb_rects[j].x = randint(40, 600)
                bomb_rects[j].y = -30
            else:
                if (bomb_rects[j].y >= 400):
                    var = j
                    morte = True
                    x_sprite_explosion = 0
                    while x_sprite_explosion <= 20:
                        x_sprite_explosion = x_sprite_explosion + 0.001
                        tela.blit(sprite_explosion, (bomb_rects[j].x, bomb_rects[j].y), (int(x_sprite_explosion)*32, 0, 32, 32)) 
                else:
                    if (bomb_rects[j].x <= 200 or bomb_rects[j].x >= 500):
                        bomb_rects[j].y = bomb_rects[j].y + 1
                    else:
                        bomb_rects[j].y = bomb_rects[j].y + 1.5
                

    pygame.display.flip()
