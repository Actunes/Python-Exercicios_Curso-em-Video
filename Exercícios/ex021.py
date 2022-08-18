#Faça um programa em python que abra e reproduza
#o audio de um arquivo mp3.

# Importando o PyGame
import pygame
import os

# Inicializando o PyGame
pygame.init()

# Carregando o arquivo MP3 e executando
if os.path.exists('ex021.mp3'):
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo ex021.mp3 não está no diretório do script Python')

    