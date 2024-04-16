import pygame
pygame.init()
pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.play()
input()
# espera o evento acabar(musica terminar) para encerrar o programa
pygame.event.wait()