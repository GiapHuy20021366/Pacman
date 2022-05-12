from numpy import index_exp
from setup.constant import*
from entity.entity import Entity
import pygame
from algorithm.collison import*

class Player(Entity):
    def __init__(self, map, pos_X=0, pos_Y=0, size=10) -> None:
        super().__init__(map, pos_X, pos_Y, size)
        self.unique_action()
        self.name = 'pink'
        self.status = {
            'UP': False,
            'DOWN': False,
            'LEFT': False,
            'RIGHT': False,
            'STAND': True
        }
        self.on_status = 'RIGHT'
        self.speed = 0.5
    
    def unique_action(self):
        actions = ['pink_pacman_right', 'pink_pacman_left', 'pink_pacman_down', 'pink_pacman_up', 'pink_pacman_stay']
        title = 'net_pacman'
        super().parse_actions((actions, title))
        
    def execute_key(self, keys):
        self.status['UP'] = keys[pygame.K_UP]
        self.status['DOWN'] = keys[pygame.K_DOWN]
        self.status['LEFT'] = keys[pygame.K_LEFT]
        self.status['RIGHT'] = keys[pygame.K_RIGHT]
        self.status['STAND'] = not(keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_DOWN] or keys[pygame.K_UP])
        
        move_space = int(self.speed * SIZE_PER_UNIT)
        
        new_rect = self.rect.copy()
        # new_rect.width = int(new_rect.width / 1.5)
        # new_rect.height = int(new_rect.width / 1.5)
        # new_rect.center = self.rect.center
        
        want_status = None
        if self.status['LEFT']:
            want_status = 'LEFT'
            new_rect.topleft = (new_rect.topleft[0] - move_space, new_rect.topleft[1])
        elif self.status['RIGHT']:
            want_status = 'RIGHT'
            new_rect.topleft = (new_rect.topleft[0] + move_space, new_rect.topleft[1])
        elif self.status['UP']:
            want_status = 'UP'
            new_rect.topleft = (new_rect.topleft[0], new_rect.topleft[1] - move_space)
        elif self.status['DOWN']:
            want_status = 'DOWN'
            new_rect.topleft = (new_rect.topleft[0], new_rect.topleft[1] + move_space)
        
        #Check collison with monsters
        if rect_collison_group(new_rect, self.map.monsters):
            # Die
            return
        
        #Check collison with walls
        collision = rect_collison_group(new_rect, self.map.walls, get=True)
        if collision is not None:
            # print(len(collision.sprites()))
            if len(collision.sprites()) == 1:
                wall = collision.sprites()[0]
                index_X = int(wall.rect.center[1] / SPACE / SIZE_PER_UNIT)
                index_Y = int(wall.rect.center[0] / SPACE / SIZE_PER_UNIT)
                # print(index_X, index_Y)
                if self.on_status == 'RIGHT':
                    if self.map.map_data["Map"][index_X][index_Y + 1] != 'x':
                        self.status[want_status] = False
                        self.status['RIGHT'] = True
                    else: return
                elif self.on_status == 'LEFT':
                    if self.map.map_data["Map"][index_X][index_Y - 1] != 'x':
                        self.status[want_status] = False
                        self.status['LEFT'] = True
                    else: return
                elif self.on_status == 'UP':
                    if self.map.map_data["Map"][index_X - 1][index_Y] != 'x':
                        self.status[want_status] = False
                        self.status['UP'] = True
                    else: return
                elif self.on_status == 'DOWN':
                    if self.map.map_data["Map"][index_X + 1][index_Y] != 'x':
                        self.status[want_status] = False
                        self.status['DOWN'] = True   
                    else: return  
            else: return
        
        
        if self.status['LEFT']:
            self.pos_X -= self.speed
            self.on_status = 'LEFT'
            self.set_action(self.name + '_pacman_left')
        elif self.status['RIGHT']:
            self.pos_X += self.speed
            self.on_status = 'RIGHT'
            self.set_action(self.name + '_pacman_right')
        elif self.status['UP']:
            self.pos_Y -= self.speed
            self.on_status = 'UP'
            self.set_action(self.name + '_pacman_up')
        elif self.status['DOWN']:
            self.pos_Y += self.speed
            self.on_status = 'DOWN'
            self.set_action(self.name + '_pacman_down')
        