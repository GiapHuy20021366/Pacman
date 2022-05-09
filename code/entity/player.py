from setup.constant import*
from entity.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, pos_X=0, pos_Y=0, size=10) -> None:
        super().__init__(pos_X, pos_Y, size)
        
    def execute_key(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos_X -= 1
        elif keys[pygame.K_RIGHT]:
            self.pos_X += 1
        elif keys[pygame.K_UP]:
            self.pos_Y -= 1
        elif keys[pygame.K_DOWN]:
            self.pos_Y += 1