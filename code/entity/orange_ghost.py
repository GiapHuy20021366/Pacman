from setup.constant import*
from entity.entity import Entity
import pygame

class OrangeGhost(Entity):
    def __init__(self, map, pos_X=0, pos_Y=0, size=10) -> None:
        super().__init__(map, pos_X, pos_Y, size)
        self.unique_action()
        
    def unique_action(self):
        actions = ['orange_pacman_right', 'orange_pacman_left', 'orange_pacman_down', 'orange_pacman_up', 'orange_pacman_stay']
        title = 'net_pacman'
        super().parse_actions((actions, title))