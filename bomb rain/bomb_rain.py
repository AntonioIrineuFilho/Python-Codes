import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.display.set_caption('BOMB RAIN')
fps = pygame.time.Clock()
tela = pygame.display.set_mode((640, 480))
pygame.mixer.music.load('soundtrack.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
sfx_collect = pygame.mixer.Sound('pickup.wav')
sfx_collect.set_volume(0.2)
sfx_explosion = pygame.mixer.Sound('boom.wav')
sfx_explosion.set_volume(0.1)
font_text = pygame.font.SysFont('Yoster Island Regular', 25, False, False)
tela_inicial = pygame.image.load('inicial.png').convert()
game_over = pygame.image.load('gameover.png').convert()
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
inicial = True
gameover = False
morte = False
cont = 1
somador_pontos = 0
recordes = [0]

while True:

    tela.blit(cenario, (0, 0))
    fps.tick(30)

    if (inicial):
        tela.blit(tela_inicial, (0, 0))
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                pygame.quit()
                exit()
            if (event.type == KEYDOWN and event.key == K_SPACE):
                inicial = False
    elif (gameover):
        cont = 1
        pontuacao = pygame.font.SysFont('Yoster Island Regular', 20, False, False).render(f'{max(recordes)}', False, (255, 255, 255))
        recorde = pygame.font.SysFont('Yoster Island Regular', 20, False, False).render(f'{somador_pontos}', False, (255, 255, 255))
        tela.blit(game_over, (0, 0))
        tela.blit(pontuacao, (435, 170))
        tela.blit(recorde, (435, 219))
        for event in pygame.event.get():
            if (event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)):
                pygame.quit()
                exit()
            if (event.type == KEYDOWN and event.key == K_SPACE):
                gameover = False
                somador_pontos = 0
    elif (morte):
        if (cont == 1):
            for k in range(len(bomb_rects)):
                if (bomb_rects[k].y >= 400):
                    x_sprite_explosion = 0
                    while x_sprite_explosion <= 20:
                        x_sprite_explosion = x_sprite_explosion + 0.001
                        tela.blit(sprite_explosion, (bomb_rects[k].x, bomb_rects[k].y), (int(x_sprite_explosion)*32, 0, 32, 32))
            sfx_explosion.play()
        if (x_sprite_personagem >= 5):
            morte = False
            gameover = True
            for k in range(len(bomb_rects)):
                bomb_rects[k].y = -50
        x_sprite_personagem = x_sprite_personagem + 0.15
        tela.blit(sprite_personagem, spr, (int(x_sprite_personagem)*96, 192, 96, 96))
        cont = cont + 1
    else:
        bomb_rects = []
        text_pontos = font_text.render(f'Pontos: {somador_pontos}', False, (0, 0, 0))
        text_recorde = font_text.render(f'Recorde: {max(recordes)}', False, (0, 0, 0)) 
        tela.blit(text_pontos, (457, 25))
        tela.blit(text_recorde, (457, 70))

        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
        
        tela.blit(sprite_personagem, spr, (int(x_sprite_personagem)*96, y_sprite_personagem, 96, 96))

        if (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]):
            x_sprite_personagem = x_sprite_personagem + 0.25
            y_sprite_personagem = 96
            spr.x = spr.x - 10
        elif (pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]):
            x_sprite_personagem = x_sprite_personagem + 0.25
            y_sprite_personagem = 0
            spr.x = spr.x + 10
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
                somador_pontos = somador_pontos + 1
                sfx_collect.play()
                if (somador_pontos > max(recordes)):
                    recordes.append(somador_pontos)
            else:
                if (bomb_rects[j].y >= 400):
                    for k in range(len(bomb_rects)):
                        if (bomb_rects[k].y >= 400):
                            x_sprite_explosion = 0
                            while x_sprite_explosion <= 20:
                                x_sprite_explosion = x_sprite_explosion + 0.001
                                tela.blit(sprite_explosion, (bomb_rects[k].x, bomb_rects[k].y), (int(x_sprite_explosion)*32, 0, 32, 32))
                    morte = True
                    
                else:
                    if (bomb_rects[j].x <= 200 or bomb_rects[j].x >= 500):
                        bomb_rects[j].y = bomb_rects[j].y + 1
                    else:
                        bomb_rects[j].y = bomb_rects[j].y + 1.5
                
    pygame.display.flip()
