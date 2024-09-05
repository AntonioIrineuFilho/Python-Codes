import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x_bombas = [randint(40, 600), randint(40, 600), randint(40, 600), randint(40, 600)]
y_bombas = [0, 0, 0, 0]
x_personagem = 300
y_personagem = 350
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('BOMB RAIN')
cenario = pygame.image.load('cenario.png').convert()
fps = pygame.time.Clock()

while True:

    bombas = []
    fps.tick(30)
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


    tela.blit(cenario, (0, 0))

    ret1 = pygame.draw.rect(tela, (255, 255, 255), (x_bombas[0], y_bombas[0], 45, 48))
    bombas.append(ret1)
    ret2 = pygame.draw.rect(tela, (0, 255, 255), (x_bombas[1], y_bombas[1], 45, 48))
    bombas.append(ret2)
    ret3 = pygame.draw.rect(tela, (255, 255, 0), (x_bombas[2], y_bombas[2], 45, 48))
    bombas.append(ret3)
    ret4 = pygame.draw.rect(tela, (255, 0, 255), (x_bombas[3], y_bombas[3], 45, 48))
    bombas.append(ret4)
    personagem = pygame.draw.rect(tela, (0, 0, 0), (x_personagem, y_personagem, 45, 100))

    for i in range(len(bombas)):
        if (bombas[i].colliderect(personagem)):
            x_bombas[i] = randint(40, 600)
            y_bombas[i] = -50
        else:
            if (y_bombas[i] >= altura-80):
                y_bombas[i] = 0
            else:
                y_bombas[i] = y_bombas[i] + 1

    pygame.display.flip()
