from setup.constant import*
from entity.entity import Entity
import pygame
class Wall(Entity):
    def __init__(self, map, pos_X=0, pos_Y=0, size = 10) -> None:
        super().__init__(map, pos_X, pos_Y, size)
        self.on_action = None
    
    def draw(self):
        # pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.pos_X * SIZE_PER_UNIT, 
        #                                                      self.pos_Y * SIZE_PER_UNIT, 
        #                                                      self.size * SIZE_PER_UNIT, 
        #                                                      self.size * SIZE_PER_UNIT))
        pass