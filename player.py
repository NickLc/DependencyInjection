import pygame
import random
import math
from pygame import mixer

class Player():
    def __init__(self):
        self.speed = 3
        self.IMG = pygame.image.load('image/space-shuttle.png').convert_alpha()
        self.X = 390
        self.Y = 480
        self.X_change = 0
        self.accel = 0
        self.ev = False

    def move(self):
        # movimiento del player
        if self.ev and self.X_change < 0:
            self.accel = self.speed/100
            self.X_change += self.accel  

        if self.ev and self.X_change > 0:
            self.accel = -self.speed/100
            self.X_change += self.accel  

        self.X += self.X_change    

        # limites de espacio de la nave
        if self.X <= 0:
                self.X = 0
        elif self.X >= 770:
                self.X = 770    
        
    def show(self, screen):
        screen.blit(self.IMG, (self.X,self.Y))


class Enemy():
    def __init__(self):
        self.speed = 2
        self.IMG = pygame.image.load('image/space-invaders.png').convert_alpha()
        self.X = random.randint(0,770)
        self.Y = random.randint(50,150)
        self.X_change = self.speed
        self.Y_change = -20
    
    def move(self):
        self.X += self.X_change    
        # limites de espacio del enemigo

        if self.X <= 0:
            self.X_change = self.speed
            self.Y -= self.Y_change
        elif self.X >= 770:
            self.X_change = -self.speed
            self.Y -= self.Y_change 

    def show(self, screen):
        screen.blit(self.IMG, (self.X,self.Y))
