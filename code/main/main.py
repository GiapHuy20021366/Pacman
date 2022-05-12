import sys,os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pygame
from entity.entity import*
from map.map import *
from setup.constant import*
from animate.source import*

def run():
    pygame.init()
    map_data = get_map_data(r'Map\Json\map.json')
    screen_width = int(map_data["Width"]) 
    screen_height = int(map_data["Height"]) 
    screen = pygame.display.set_mode([SIZE_PER_UNIT*SPACE*screen_width, 
                                    SIZE_PER_UNIT*SPACE*screen_height],
                                    pygame.RESIZABLE
                                    )
    # screen = pygame.display.set_mode([560, 
    #                                 620],
    #                                 pygame.RESIZABLE
    #                                 )
    background_img = pygame.image.load(r'Map\png\maze.png')
    bg = pygame.transform.scale(background_img, [SIZE_PER_UNIT*SPACE*screen_width, 
                                    SIZE_PER_UNIT*SPACE*screen_height])
    load_source(r'Sprite\net_pacman.png', r'Sprite\net_pacman.json')
    map = Map(screen, map_data)
    map.load_map()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        key = pygame.key.get_pressed()
        screen.fill((0,0,0))
        screen.blit(bg, (0,0))
        map.draw()
        map.update()
        map.execute_key(key)
        pygame.display.flip()
        clock.tick(60)
            

if __name__ == '__main__':
    run()
        
        
    