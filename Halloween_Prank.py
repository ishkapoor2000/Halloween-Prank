"""
Created on Fri Oct 30 19:41:32 2020
@author: ISH KAPOOR
"""
import pygame
from pygame import mixer
from time import sleep

pygame.init()
window = pygame.display.set_mode((600, 600))
# window = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)

pygame.mixer.init()
pygame.mixer_music.load('C:/Users/ISH KAPOOR/Desktop/GIT Project/Halloween Project/ratsasan.mp3') # Not so scary audio
pygame.mixer_music.play()
sleep(5)

pygame.mixer_music.load('C:/Users/ISH KAPOOR/Desktop/GIT Project/Halloween Project/scary.mp3') # Scary audio
pygame.mixer_music.play()
sleep(1)

image = pygame.image.load('C:/Users/ISH KAPOOR/Desktop/GIT Project/Halloween Project/scr2.jpg') # Scary image(size: 200x200)
window.blit(image, (10, 10))
pygame.display.update()
sleep(3)