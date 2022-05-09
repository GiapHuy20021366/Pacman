import sys,os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from animate.animation import Animation
from animate.source import get_action_frames
class Action:
    def __init__(self, name_action =  None, title = 'net_pacman', animate = (1.0, -1)) -> None:
        self.images = get_action_frames(name_action, title)
        self.index = 0;
        self.animation = Animation(animate, self)
    
    def length(self):
        return len(self.images)
    
    def get_img(self):
        self.animation.update()
        return self.images[self.index]
    