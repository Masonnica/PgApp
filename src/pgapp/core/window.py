import pygame

from .config import get_config, get_root_dir
from .scene import Scene


FLAG_WINDOWED = 0
FLAG_MINIMIZED = 1
FLAG_MAXIMIZED = 2
FLAG_FULLSCREEN = 3


class Window:
    def __init__(self, title: str, scene: "Scene"):
        size = (
            get_config()["display"]["window_size"]["x"],
            get_config()["display"]["window_size"]["y"],
        )
        self.window = pygame.Window(title, size, )
    
    def update(self):
        pass
    
    def close(self):
        pass
