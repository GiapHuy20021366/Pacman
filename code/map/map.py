import sys,os

from entity.blue_ghost import BlueGhost
from entity.pink_ghost import PinkGhost
from entity.orange_ghost import OrangeGhost
from entity.red_ghost import RedGhost
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pygame
from entity.entity import*
from entity.wall import*
from entity.player import*
from setup.constant import*
import json

def get_map_data(json_path):
    map_data = None
    with open(json_path, 'r') as f:
        map_data = json.load(f)
    return map_data
class Map():
        
    def __init__(self, screen, map_data) -> None:
        self.screen = screen
        self.walls = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.players = pygame.sprite.GroupSingle()
        self.map_data = map_data
    
    
    def load_map(self):
        map = self.map_data["Map"]
        print(len(map[0]), len(map))
        for row, row_entity in enumerate(map):
            for col, char in enumerate(row_entity):
                pos_X = col * SPACE
                pos_Y = row * SPACE
                if char not in self.map_data: continue
                entity = self.map_data[char]
                if entity == 'Wall':
                    self.walls.add(Wall(self, pos_X, pos_Y))
                elif entity == 'Player':
                    self.players.add(Player(self, pos_X, pos_Y))     
                elif entity == 'Monster':
                    self.monsters.add(Player(self, pos_X, pos_Y))    
                elif entity == 'BlueGhost':
                    self.monsters.add(BlueGhost(self, pos_X, pos_Y))  
                elif entity == 'OrangeGhost':
                    self.monsters.add(OrangeGhost(self, pos_X, pos_Y))
                elif entity == 'RedGhost':
                    self.monsters.add(RedGhost(self, pos_X, pos_Y))
                elif entity == 'PinkGhost':
                    self.monsters.add(PinkGhost(self, pos_X, pos_Y))
        # for player in self.players.sprites():
        #     player.parse_actions((['yellow_pacman'], 'net_pacman'))
        # for monster in self.monsters.sprites():
        #     monster.parse_actions((['yellow_pacman'], 'net_pacman'))
                          
    def set_background():
        pass
    
    def draw(self):
        # self.walls.draw(self.screen)
        self.dots.draw(self.screen)
        self.players.draw(self.screen)
        self.monsters.draw(self.screen)
    
    def update(self):
        self.walls.update()
        self.dots.update()
        self.players.update()
        self.monsters.update()
    
    def execute_key(self, key):
        for sprite in self.players.sprites():
            sprite.execute_key(key)

  