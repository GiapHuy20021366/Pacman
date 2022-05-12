import sys,os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pygame
from setup.constant import*
from animate.animation import*
from animate.action import*
class Entity(pygame.sprite.Sprite):
    
    def __init__(self, map, pos_X = 0, pos_Y = 0, size = 10, actions = None):
        super().__init__()
        self.map = map
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.size = size
        self.actions = dict({})
        
        self.image = pygame.Surface((size*SIZE_PER_UNIT, size*SIZE_PER_UNIT))
        # self.image.fill((0,255,0))
        self.on_action = None
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_X * SIZE_PER_UNIT, self.pos_Y * SIZE_PER_UNIT]

        if actions is not None:
            self.parse_actions(actions)
        
    def parse_actions(self, actions):
        name_actions, title = actions
        for name_action in name_actions:
            action = Action(name_action, title)
            self.add_action(name_action, action)
        
    def add_action(self, name_action, action):
        self.actions[name_action] = action
        if self.on_action is None:
            self.on_action = action
    
    def set_action(self, action_name):
        if action_name in self.actions:
            self.on_action = self.actions[action_name]
     
    def update(self):
        if self.on_action is not None: 
            self.image = self.on_action.get_img()
        self.image = pygame.transform.scale(self.image, (self.size * SIZE_PER_UNIT, self.size * SIZE_PER_UNIT))
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_X * SIZE_PER_UNIT, self.pos_Y * SIZE_PER_UNIT]
        
        
    def destroy(self):
        for action_name in self.actions:
            self.actions[action_name].stop()

        
