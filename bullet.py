
import pygame
import random
import math
from pygame import mixer

fire_address = 'image/bullet-fire.png'
ice_address = 'image/bullet-ice.png'
poison_address = 'image/bullet-posion.png'

class Bullet():
    def __init__(self, posY, address):
        self.speed = 4        
        # ready - no se ve en pantalla
        # fire - se ve
        self.IMG = pygame.image.load(address).convert_alpha()
        self.X = 0
        self.Y = posY
        self.Y_change = self.speed
        self.state = "ready"

    def move(self,screen,posY):
        # movimiento de bullet
        if self.Y < 0 :
            self.Y = posY
            self.state = "ready"

        if self.state is "fire":
            self.show(screen)
            self.Y -= self.Y_change
    
    def show(self, screen):
        self.state = "fire"
        screen.blit(self.IMG, (self.X+8, self.Y+5))

class FireBullet(Bullet):
    def __init__(self, posY, address=fire_address):
        super().__init__(posY, address)

    def move(self, screen, posY):
        return super().move(screen, posY)
    
    def show(self, screen):
        return super().show(screen)

class IceBullet(Bullet):
    def __init__(self, posY, address=ice_address):
        super().__init__(posY, address)

    def move(self, screen, posY):
        return super().move(screen, posY)
    
    def show(self, screen):
        return super().show(screen)

class PoisonBullet(Bullet):
    def __init__(self, posY, address=poison_address):
        super().__init__(posY, address)

    def move(self, screen, posY):
        return super().move(screen, posY)
    
    def show(self, screen):
        return super().show(screen)