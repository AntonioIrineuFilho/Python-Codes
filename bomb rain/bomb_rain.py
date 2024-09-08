import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.display.set_caption('BOMB RAIN')
tela = pygame.display.set_mode((640, 480))
cenario = pygame.image.load('cenario.png').convert()
sprite_explosion = pygame.image.load('explosion.png').convert_alpha()
sprite_personagem = pygame.image.load('personagem.png').convert_alpha()
spr = sprite_personagem.get_rect(topleft=(300, 350))
sprite_bomb = pygame.image.load('bomb.png').convert_alpha()
sbrs = []
for i in range(0, 6):
    sbrs.append(sprite_bomb.get_rect(topleft=(randint(40, 600), 0)))
x_sprite_bomb = 0
y_sprite_bomb = 0
x_sprite_personagem = 0
y_sprite_personagem = 0



while True:
    pygame.time.Clock().tick(30)
    bomb_rects = []
    tela.blit(cenario, (0, 0))

    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            exit()
        if (event.type == KEYDOWN):
            if (event.key == K_a):
                x_personagem = x_personagem - 10
            if (event.key == K_d):
                x_personagem = x_personagem + 10

    if (pygame.key.get_pressed()[K_a]):
        x_personagem = x_personagem - 10
    if (pygame.key.get_pressed()[K_d]):
        x_personagem = x_personagem + 10

    for i in range(0, 6):
        tela.blit(sprite_bomb, sbrs[i], (int(x_sprite_bomb)*32, y_sprite_bomb, 32, 32))
        bomb_rects.append(sbrs[i])

    tela.blit(sprite_personagem, spr, (int(x_sprite_personagem)*96, y_sprite_personagem+288, 96, 96))

    x_sprite_personagem = x_sprite_personagem + 0.2
    if (x_sprite_personagem >= 3):
        x_sprite_personagem = 0

    x_sprite_bomb = x_sprite_bomb + 0.25
    if (x_sprite_bomb == 2):
        x_sprite_bomb = 0

    for j in range(len(bomb_rects)):
        if (bomb_rects[j].colliderect(spr)):
            bomb_rects[j].x = randint(40, 600)
            bomb_rects[j].y = -50
        else:
            if (bomb_rects[j].y >= 400):
                x_sprite_explosion = 0
                while x_sprite_explosion <= 20:
                    x_sprite_explosion = x_sprite_explosion + 0.001
                    tela.blit(sprite_explosion, (bomb_rects[j].x, bomb_rects[j].y), (int(x_sprite_explosion)*32, 0, 32, 32))
                bomb_rects[j].y = -50
            else:
                if (j % 2 == 0):
                    bomb_rects[j].y = bomb_rects[j].y + 0.4
                if (bomb_rects[j].y > 250):
                    bomb_rects[j].y = bomb_rects[j].y + 0.8
                else:
                    bomb_rects[j].y = bomb_rects[j].y + 1
                    if (bomb_rects[j].y > 250):
                        bomb_rects[j].y = bomb_rects[j].y + 0.3

    pygame.display.flip()
