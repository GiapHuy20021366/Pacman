from setup.constant import*
from entity.entity import Entity
import pygame

class RedGhost(Entity):
    def __init__(self, map, pos_X=0, pos_Y=0, size=10) -> None:
        super().__init__(map, pos_X, pos_Y, size)
        self.unique_action()
        
    def unique_action(self):
        actions = ['red_pacman_right', 'red_pacman_left', 'red_pacman_down', 'red_pacman_up', 'red_pacman_stay']
        title = 'net_pacman'
        super().parse_actions((actions, title))