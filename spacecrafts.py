import pygame
import random
import math
from pygame import mixer
from bullets import IceBullet, FireBullet, PoisonBullet, Bullet

class SpaceCraft():
    def __init__(self, bullet:Bullet, address):
        
        self.IMG = pygame.image.load(address).convert_alpha()
        self.X = 0
        self.Y = 0

    def move(self):
        pass

    def show(self,screen):
        screen.blit(self.IMG, (self.X,self.Y))

spaceShuttle = 'image/space-shuttle.png'

class Player(SpaceCraft):
    def __init__(self, bullet, address=spaceShuttle):
        super().__init__(bullet, address)
        self.speed = 3
        self.X = 390
        self.Y = 480
        self.X_change = 0
        self.accel = 0
        self.ev = False
        self.bullet = bullet
        
        
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

    def shoot(self, screen):
        self.bullet.speed = -4     # player bullet goes up
        # Init in the same position from player
        self.bullet.X = self.X
        self.bullet.Y = self.Y
        # Star bullet   
        self.bullet.state = "shoot"     
        self.bullet.show(screen)
        
    def check_Bullet(self, screen):
        self.bullet.move(screen)

    def show(self, screen):
        return super().show(screen)
    
    def action(self, screen):
        self.move()
        self.check_Bullet(screen)
        self.show(screen)


fire_address = 'image/space-fire-invaders.png'
ice_address = 'image/space-ice-invaders.png'
poison_address = 'image/space-poison-invaders.png'

class Enemy(SpaceCraft):
    def __init__(self, bullet, address, element):
        super().__init__(bullet, address)
        self.speed = 2
        self.X = random.randint(0,770)
        self.Y = random.randint(50,150)
        self.X_change = self.speed
        self.Y_change = -20
        self.element = element
        self.bullet = bullet
        self.bullet.speed = 4     # player bullet goes down

    def move(self):
        self.X += self.X_change    
        # limites de espacio del enemigo

        if self.X <= 0:
            self.X_change = self.speed
            self.Y -= self.Y_change
        elif self.X >= 770:
            self.X_change = -self.speed
            self.Y -= self.Y_change

    def shoot(self, screen):
        # Init in the same position from player
        self.bullet.X = self.X
        self.bullet.Y = self.Y
        # Star bullet   
        self.bullet.state = "shoot"     
        self.bullet.show(screen)

    def check_Bullet(self, screen):   # this funtion allways calls  
        self.bullet.move(screen)

    def show(self, screen):
        screen.blit(self.IMG, (self.X,self.Y))

class FireEnemy(Enemy):
    def __init__(self, bullet, address=fire_address, element="fire"):
        super().__init__(bullet, address=address, element=element)
    
    def move(self):
        return super().move()

    def shoot(self, screen):
        return super().shoot(screen)

    def check_Bullet(self, screen):
        return super().check_Bullet(screen)

    def show(self, screen):
        return super().show(screen)

class IceEnemy(Enemy):
    def __init__(self, bullet, address=ice_address, element="ice"):
        super().__init__(bullet, address=address, element=element)
    
    def move(self):
        return super().move()
    
    def shoot(self, screen):
        return super().shoot(screen)

    def check_Bullet(self, screen):
        return super().check_Bullet(screen)

    def show(self, screen):
        return super().show(screen)

class PoisonEnemy(Enemy):
    def __init__(self, bullet, address=poison_address, element="poison"):
        super().__init__(bullet, address=address, element=element)
    
    def move(self):
        return super().move()
    
    def shoot(self, screen):
        return super().shoot(screen)

    def check_Bullet(self, screen):
        return super().check_Bullet(screen)

    def show(self, screen):
        return super().show(screen)