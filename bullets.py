
import pygame
import random
import math
from pygame import mixer

fire_address = 'image/bullet-fire.png'
ice_address = 'image/bullet-ice.png'
poison_address = 'image/bullet-poison.png'

class Bullet():
    def __init__(self, address):
        self.speed = 0  # speed depend from type spaceCraft     
        # ready - no se ve en pantalla
        # fire - se ve
        self.IMG = pygame.image.load(address).convert_alpha()
        self.X = 0
        self.Y = 0
        self.state = "ready"

    def move(self,screen):
        # movimiento de bullet
        if self.Y < 0 :
            self.Y = 0
            self.state = "ready"

        if self.state is "fire":
            self.show(screen)
            self.Y += self.speed
    
    def show(self, screen):
        screen.blit(self.IMG, (self.X+8, self.Y+5))

class FireBullet(Bullet):
    def __init__(self, address=fire_address):
        super().__init__( address)

    def move(self, screen):
        return super().move(screen)
    
    def show(self, screen):
        return super().show(screen)

class IceBullet(Bullet):
    def __init__(self, address=ice_address):
        super().__init__(address)

    def move(self, screen):
        return super().move(screen)
    
    def show(self, screen):
        return super().show(screen)

class PoisonBullet(Bullet):
    def __init__(self, address=poison_address):
        super().__init__(address)

    def move(self, screen):
        return super().move(screen)
    
    def show(self, screen):
        return super().show(screen)