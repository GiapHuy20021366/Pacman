import sys,os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import pygame
from entity.entity import*
from map.map import Map
from setup.constant import*
from animate.source import*

def run():
    pygame.init()
    screen = pygame.display.set_mode([SIZE_PER_UNIT*SPACE*25, 
                                          SIZE_PER_UNIT*SPACE*13],
                                         pygame.RESIZABLE)
    load_source(r'Sprite\net_pacman.png', r'Sprite\net_pacman.json')
    map = Map(screen)
    map.load_map()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        key = pygame.key.get_pressed()
        screen.fill((0,0,0))
        map.draw()
        map.update()
        map.execute_key(key)
        pygame.display.flip()
        clock.tick(60)
            

if __name__ == '__main__':
    run()
        
        
    