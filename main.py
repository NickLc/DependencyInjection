import pygame
import random
import math
from pygame import mixer
from spacecrafts import Player, Enemy, IceEnemy, FireEnemy, PoisonEnemy
from statistics import Data
from bullets import FireBullet, IceBullet, PoisonBullet
import dependency_injector.containers as containers
import dependency_injector.providers as providers
from container import Crafts,Powers,Enemies


class Set_Enemy():
    def __init__(self):
        self.nro_of_enemies = 18
        self.nro_enemies_for_type = int(self.nro_of_enemies/3)

        self.enemyFire = [Enemies.fire() for i in range(self.nro_enemies_for_type)]
        self.enemyIce = [Enemies.ice() for i in range(self.nro_enemies_for_type)]
        self.enemyPoison = [Enemies.poison() for i in range(self.nro_enemies_for_type)]
        self.enemies = self.enemyFire + self.enemyIce + self.enemyPoison

        self.delay_shoot = 0
        self.enemy_shoot = random.choice(self.enemies)

    def action(self, screen, player, data):
        
        for enemy in self.enemies:
            enemy.move()
            enemy.show(screen)
            self.collition_kill_enemy(enemy, player, data)
            self.collition_kill_player(self.enemy_shoot,player,data,screen)
            
        delay = random.randint(100,200)

        if self.delay_shoot > delay:      # Init bullet
            self.enemy_shoot.shoot(screen)
            self.delay_shoot = 0
            self.enemy_shoot = random.choice(self.enemies)

        self.enemy_shoot.check_Bullet(screen)

    def collition_kill_enemy(self,enemy,player,data):

        if self.iscollision(enemy, player.bullet):
            explosion_Sound = mixer.Sound('sound/explosion.wav')
            explosion_Sound.play()
            player.bullet.Y = player.Y
            player.bullet.state = "ready"
            if  enemy.element == player.bullet.element:
                data.update_score()      
                enemy.X = random.randint(0,770)
                enemy.Y = random.randint(50,150)
        
    def collition_kill_player(self,enemy,player,data,screen):

        if self.iscollision(player, enemy.bullet):
            # GAME OVER
            explosion_Sound = mixer.Sound('sound/explosion.wav')
            explosion_Sound.play()
            self.delete()
            data.show_game_over(screen)

    def delete(self):
        for enemy in self.enemies:
            enemy.Y = 2000
        self.enemy_shoot.Y=2000


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
        self.player = Crafts.ice()
        #self.player = Player(FireBullet())
        # Load Enemy
        self.setEnemies = Set_Enemy()
        # Load Statistics
        self.data = Data()
        #bullet change
        self.change = 1  


    def play(self):
        # Game Loop
        running = True
        
        while running:
            self.setEnemies.delay_shoot +=1
            # RGB-Background color
            self.screen.fill((30,80,180))
            # Add background
            self.screen.blit(self.background,(0,0))
            # Add and Show FPS
            self.fpsnumber = self.clock.get_fps()
            self.fps = self.fpsfont.render("fps:"+str(math.ceil(self.fpsnumber)),True,pygame.Color('white'))
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

                    if event.key == pygame.K_SPACE:  # Activation shoot
                        # Only shoot when state from bullet is ready
                        if self.player.bullet.state is "ready":                           
                            self.player.shoot(self.screen)
                            player_shoot_Sound = mixer.Sound('sound/laser.wav')
                            player_shoot_Sound.play()

                    if event.key == pygame.K_z:  
                        if self.player.bullet.state is "ready": 
                            if self.change == 1:
                                self.player.bullet = Powers.ice()
                                self.change = (self.change+1)%4
                            elif self.change == 2:
                                self.player.bullet = Powers.poison()
                                self.change = (self.change+1)%3
                            elif self.change == 0:
                                self.player.bullet = Powers.fire()
                                self.change = (self.change+1)%3    

                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and event.key == lastkey:                
                        self.player.ev = True

            self.player.action(self.screen)
            self.setEnemies.action(self.screen, self.player,self.data)
            self.modo = self.fpsfont.render('Modo: '+self.player.bullet.__class__.__name__, False, (255, 0, 0))
            self.screen.blit(self.modo,(220,10))            
            self.data.show_score(self.screen)
            self.__gameOver__()
            pygame.display.update()
    
    def __gameOver__(self):
        for enemy in self.setEnemies.enemies:
            # GAME OVER
            if enemy.Y > 440:
                self.setEnemies.delete()
                self.data.show_game_over(self.screen)
                break
        
def main():
    game = App_Game()
    game.play()

if __name__ == "__main__":
    main() 
