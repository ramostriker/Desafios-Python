# Faça um programa em Python queabra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
# Substitua musica.mp3 pelo nome do arquivo.mp3
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
