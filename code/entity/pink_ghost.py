from setup.constant import*
from entity.entity import Entity
import pygame

class PinkGhost(Entity):
    def __init__(self, map, pos_X=0, pos_Y=0, size=10) -> None:
        super().__init__(map, pos_X, pos_Y, size)
        self.unique_action()
        
    def unique_action(self):
        actions = ['pink_pacman_right', 'pink_pacman_left', 'pink_pacman_down', 'pink_pacman_up', 'pink_pacman_stay']
        title = 'net_pacman'
        super().parse_actions((actions, title))