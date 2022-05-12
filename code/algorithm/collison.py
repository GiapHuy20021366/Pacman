
import pygame

def rect_collison_group(rect, group, get = False):
    group_collison = pygame.sprite.Group()
    for sprite in group.sprites():
        if pygame.Rect.colliderect(rect, sprite.rect):
            group_collison.add(sprite)
            if not get: return True
    if get: return group_collison if len(group_collison.sprites()) != 0 else None
    return False