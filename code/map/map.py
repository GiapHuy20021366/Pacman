import sys,os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pygame
from entity.entity import*
from entity.wall import*
from entity.player import*
from setup.constant import*


map = (['w', 'w', 'w', 'w', 'w'],
       ['w', ' ', ' ', ' ', 'w'],
       ['w', ' ', ' ', ' ', 'w'],
       ['w', ' ', ' ', ' ', 'w'],
       ['w', 'p', ' ', ' ', 'w'],
       ['w', 'w', 'w', 'w', 'w'])
class Map():
        
    def __init__(self, screen) -> None:
        self.screen = screen
        self.walls = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
       
    def load_map(self):
        for row, row_entity in enumerate(map):
            for col, entity in enumerate(row_entity):
                pos_X = col * SPACE
                pos_Y = row * SPACE
                if entity == 'w':
                    self.walls.add(Wall(pos_X, pos_Y))
                elif entity == 'p':
                    self.player.add(Player(pos_X, pos_Y))         
        for player in self.player.sprites():
            player.parse_actions((['yellow_pacman'], 'net_pacman'))
                          
    def set_background():
        pass
    
    def draw(self):
        self.walls.draw(self.screen)
        self.dots.draw(self.screen)
        self.player.draw(self.screen)
    
    def update(self):
        self.walls.update()
        self.dots.update()
        self.player.update()
    
    def execute_key(self, key):
        for sprite in self.player.sprites():
            sprite.execute_key(key)

        