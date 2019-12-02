import pygame
import random
import math
from pygame import mixer
from spacecrafts import Player, Enemy
from statistics import Data
from bullets import FireBullet, IceBullet

class Set_Enemy():
    def __init__(self):
        self.nro_of_enemies = 20
        self.enemy = [Enemy() for i in range(self.nro_of_enemies)]

    def move(self, screen, player, data):
        # movimiento del enemigo
        for i in range(self.nro_of_enemies):
            
            self.enemy[i].move()
            
            # Colision
            collition = self.iscollision(self.enemy[i], player.bullet)
            
            if collition:
                explosion_Sound = mixer.Sound('sound/explosion.wav')
                explosion_Sound.play()
                player.bullet.Y = player.Y
                player.bullet.state = "ready"
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
        self.player = Player(FireBullet(480))
    
        # Enemy
        self.enemies = Set_Enemy()
        # Datos
        self.data = Data()
        self.game_over = False

    def play(self):
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
                        if self.player.bullet.state is "ready":
                            self.player.bullet.X = self.player.X
                            self.player.bullet.show(self.screen)
                            bullet_Sound = mixer.Sound('sound/laser.wav')
                            bullet_Sound.play()

                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and event.key == lastkey:                
                        self.player.ev = True

            self.player.move()
            
            self.game_over = self.__gameOver__()
            # movimiento del enemigo
            self.enemies.move(self.screen, self.player,self.data)

            self.player.bullet.move(self.screen, self.player.Y)
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