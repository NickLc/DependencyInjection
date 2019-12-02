import pygame
import random
import math
from pygame import mixer
    
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
