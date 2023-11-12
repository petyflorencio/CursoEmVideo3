#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

#não tenho música no meu pc RSRS

import pygame
pygame.init()
pygame.mixer.music.load('música.mp3')
pygame.mixer.music.play()
pygame.event.wait()