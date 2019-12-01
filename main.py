import pygame
import random
import math
from pygame import mixer

bullet_state = "ready"
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

class Set_Enemy():
    def __init__(self):
        self.nro_of_enemies = 20
        self.enemy = [Enemy() for i in range(self.nro_of_enemies)]

    def move(self, screen, bullet, player, data):
        global bullet_state
        # movimiento del enemigo
        for i in range(self.nro_of_enemies):
            
            self.enemy[i].move()
            
            # Colision
            collition = self.iscollision(self.enemy[i], bullet)
            
            if collition:
                explosion_Sound = mixer.Sound('sound/explosion.wav')
                explosion_Sound.play()
                bullet.Y = player.Y
                bullet_state = "ready"
                data.update_score()      
                self.enemy[i].X = random.randint(0,770)
                self.enemy[i].Y = random.randint(50,150)

            self.enemy[i].show(screen)
    
    def iscollision(self,enemy,bullet):
        distance = math.sqrt( math.pow(bullet.X-enemy.X,2) + math.pow(bullet.Y-enemy.Y,2) )
        if distance < 22:
            return True
        else:
            return False
            
class Bullet():
    def __init__(self, posY):
        self.speed = 4        
        # ready - no se ve en pantalla
        # fire - se ve
        self.IMG = pygame.image.load('image/bullet.png').convert_alpha()
        self.X = 0
        self.Y = posY
        self.Y_change = self.speed

    def move(self,screen,posY):
        global bullet_state
        # movimiento de bullet
        if self.Y < 0 :
            self.Y = posY
            bullet_state = "ready"

        if bullet_state is "fire":
            self.show(screen)
            self.Y -= self.Y_change
    
    def show(self, screen):
        global bullet_state
        bullet_state = "fire"
        screen.blit(self.IMG, (self.X+8, self.Y+5))
    
class Data():
    def __init__(self):
        self.score_val = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score_txt = self.font.render("Score :"+str(self.score_val),True,(255,255,255))
        # Game over
        self.over_font = pygame.font.Font('freesansbold.ttf',64)
        self.over_txt = self.over_font.render("GAME OVER",True,(255,255,255))

    def update_score(self):
        self.score_val += 1
        self.score_txt = self.font.render("Score :"+str(self.score_val),True,(255,255,255))

    def show_score(self,screen):
        textX, textY = 10, 10
        screen.blit(self.score_txt, (textX, textY))

    def show_game_over(self,screen):
        screen.blit(self.over_txt, (230,200))

class App_Game():
    def __init__(self):
        # Iniciar pygame
        pygame.init()
        # Crear ventana(X,Y)
        self.screen = pygame.display.set_mode((800,600))
        # Agregando fondo
        self.background = pygame.image.load('image/background.png').convert()
        # Musica de fondo
        mixer.music.load('sound/background.wav')
        mixer.music.play(-1)
        # Titulo e icono
        pygame.display.set_caption("Space invaders")
        self.icon = pygame.image.load('image/alien.png')
        pygame.display.set_icon(self.icon)
        # Mostrar fps
        self.fpsfont = pygame.font.Font('freesansbold.ttf',30)
        self.clock = pygame.time.Clock()
        pygame.display.flip()
        # Player
        self.player = Player()
        # Bullet
        self.bullet = Bullet(self.player.Y)
        # Enemy
        self.enemies = Set_Enemy()
        # Datos
        self.data = Data()
        self.game_over = False

    def play(self):
        global bullet_state
        # Game Loop
        running = True
        while running:
            # RGB-Background color
            self.screen.fill((30,80,180))
            # Agregando background
            self.screen.blit(self.background,(0,0))
            # FPS
            self.fpsnumber = self.clock.get_fps()
            self.fps = self.fpsfont.render(str(self.fpsnumber),True,pygame.Color('white'))
            self.screen.blit(self.fps,(50,50))
            self.clock.tick(120)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Movimiento/disparo
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_LEFT:
                        self.player.X_change = -self.player.speed
                        lastkey = event.key
                        self.player.ev = False

                    if event.key == pygame.K_RIGHT:
                        self.player.X_change = self.player.speed
                        lastkey = event.key
                        self.player.ev = False

                    if event.key == pygame.K_SPACE:
                        if bullet_state is "ready":
                            self.bullet.X = self.player.X
                            self.bullet.show(self.screen)
                            bullet_Sound = mixer.Sound('sound/laser.wav')
                            bullet_Sound.play()

                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and event.key == lastkey:                
                        self.player.ev = True

            self.player.move()
            
            self.game_over = self.__gameOver__()
            # movimiento del enemigo
            self.enemies.move(self.screen, self.bullet, self.player,self.data)

            self.bullet.move(self.screen, self.player.Y)
            self.player.show(self.screen)
            self.data.show_score(self.screen)
            pygame.display.update()
    
    def __gameOver__(self):
        # movimiento del enemigo
        game_over = False
        for i in range(self.enemies.nro_of_enemies):
            # GAME OVER
            if self.enemies.enemy[i].Y > 440:
                for j in range(self.enemies.nro_of_enemies):
                    self.enemies.enemy[j].Y = 2000
                self.data.show_game_over(self.screen)
                game_over = True
                return game_over
                #break
        
def main():
    game = App_Game()
    game.play()

if __name__ == "__main__":
    main() 