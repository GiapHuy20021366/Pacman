from setup.constant import*
from entity.entity import Entity
import pygame

class BlueGhost(Entity):
    def __init__(self, map, pos_X=0, pos_Y=0, size=10) -> None:
        super().__init__(map, pos_X, pos_Y, size)
        self.unique_action()
        
    def unique_action(self):
        actions = ['blue_pacman_right', 'blue_pacman_left', 'blue_pacman_down', 'blue_pacman_up', 'blue_pacman_stay']
        title = 'net_pacman'
        super().parse_actions((actions, title))