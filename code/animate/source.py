


source_img = []
datas_json = []
titles = dict({})

import pygame
import json



def load_source(PATH_IMG, PATH_JSON, title = 'net_pacman'):
    if title in titles: pass
    # Load img, data
    source_img.append(pygame.image.load(PATH_IMG).convert_alpha())
    titles[title] = len(titles)
    f = open(PATH_JSON)
    datas_json.append(json.load(f))
    f.close()
    
def get_action_frames(action_name, title = 'net_pacman'):
    if title not in titles: pass
    index = titles[title]
    data = datas_json[index]
    action_names = data['Actions']['Names']
    if action_name not in action_names: pass
    inf_frames = data['Actions'][action_name]
    img = source_img[index]
    frames = []
    for inf_frame in inf_frames:
        suf = clip(img, inf_frame)
        frames.append(suf)
    return frames
    
def clip(surface, sizes = (0,0,0,0)): 
    handle_surface = surface.copy() 
    clipRect = pygame.Rect(sizes) 
    handle_surface.set_clip(clipRect) 
    image = surface.subsurface(handle_surface.get_clip())
    return image.copy() 

