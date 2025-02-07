#Faça um programa em python que abra e reproduza o aúdio de um arquivo mp3.
import pygame

pygame.init()
pygame.mixer.music.load() #insira em aspas o nome do arquivo, não coloquei porque não tenho mp3 no meu SSD.
pygame.mixer.music.play()
pygame.event.wait() 
