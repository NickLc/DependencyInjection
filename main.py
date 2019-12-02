import pygame
import random
import math
from pygame import mixer
from spacecrafts import Player, Enemy, IceEnemy
from statistics import Data
from bullets import FireBullet, IceBullet, PoisonBullet

class Set_Enemy():
    def __init__(self):
        self.nro_of_enemies = 20
        self.enemy = [IceEnemy(FireBullet()) for i in range(self.nro_of_enemies)]
        self.delay_shoot = 0
        self.enemy_shoot = self.enemy[0]

    def action(self, screen, player, data):
        delay = random.randint(200,300)

        if self.delay_shoot > delay:      # Init bullet
            self.enemy_shoot.shoot(screen)
            self.delay_shoot = 0

        self.enemy_shoot.check_Bullet(screen)

        for i in range(self.nro_of_enemies):
            
            self.enemy[i].move()
            self.enemy[i].show(screen)

            # Collition
            collition_kill_enemy = self.iscollision(self.enemy[i], player.bullet)
            
            if collition_kill_enemy:
                explosion_Sound = mixer.Sound('sound/explosion.wav')
                explosion_Sound.play()
                player.bullet.Y = player.Y
                player.bullet.state = "ready"
                data.update_score()      
                self.enemy[i].X = random.randint(0,770)
                self.enemy[i].Y = random.randint(50,150)

              
            collition_kill_player = self.iscollision(player, self.enemy_shoot.bullet)
            if collition_kill_player:
                # GAME OVER
                explosion_Sound = mixer.Sound('sound/explosion.wav')
                explosion_Sound.play()
                self.delete()
                data.show_game_over(screen)

    def delete(self):
        for j in range(self.nro_of_enemies):
            self.enemy[j].Y = 2000

    def iscollision(self,objective,bullet):
        distance = math.sqrt( math.pow(bullet.X-objective.X,2) + math.pow(bullet.Y-objective.Y,2) )
        if distance < 22:
            return True
        else:
            return False
            

class App_Game():
    def __init__(self):
        # Init pygame
        pygame.init()
        # Create Window(X,Y)
        self.screen = pygame.display.set_mode((800,600))
        # Image of Background
        self.background = pygame.image.load('image/background.png').convert()
        # Music of Background
        mixer.music.load('sound/background.wav')
        mixer.music.play(-1)
        # Title and icon
        pygame.display.set_caption("Space invaders")
        self.icon = pygame.image.load('image/alien.png')
        pygame.display.set_icon(self.icon)
        # Load fps
        self.fpsfont = pygame.font.Font('freesansbold.ttf',30)
        self.clock = pygame.time.Clock()
        pygame.display.flip()
        # Load Player
        self.player = Player(FireBullet())
        # Load Enemy
        self.enemies = Set_Enemy()
        # Load Statistics
        self.data = Data()

    def play(self):
        # Game Loop
        running = True
        
        while running:
            self.enemies.delay_shoot +=1
            # RGB-Background color
            self.screen.fill((30,80,180))
            # Add background
            self.screen.blit(self.background,(0,0))
            # Add and Show FPS
            self.fpsnumber = self.clock.get_fps()
            self.fps = self.fpsfont.render(str(self.fpsnumber),True,pygame.Color('white'))
            self.screen.blit(self.fps,(50,50))
            self.clock.tick(120)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Move/shoot
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_LEFT:
                        self.player.X_change = -self.player.speed
                        lastkey = event.key
                        self.player.ev = False

                    if event.key == pygame.K_RIGHT:
                        self.player.X_change = self.player.speed
                        lastkey = event.key
                        self.player.ev = False

                    if event.key == pygame.K_SPACE:  # Activarion shoot
                        # Only shoot when state from bullet is ready
                        if self.player.bullet.state is "ready":
                            self.player.shoot(self.screen)
                            player_shoot_Sound = mixer.Sound('sound/laser.wav')
                            player_shoot_Sound.play()

                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and event.key == lastkey:                
                        self.player.ev = True

            self.player.action(self.screen)
            self.enemies.action(self.screen, self.player,self.data)
            
            self.data.show_score(self.screen)
            self.__gameOver__()
            pygame.display.update()
    
    def __gameOver__(self):
        for i in range(self.enemies.nro_of_enemies):
            # GAME OVER
            if self.enemies.enemy[i].Y > 440:
                self.enemies.delete()
                self.data.show_game_over(self.screen)
                break
        
def main():
    game = App_Game()
    game.play()

if __name__ == "__main__":
    main() 