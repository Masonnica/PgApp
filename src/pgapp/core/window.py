import pygame

from .config import get_config, get_root_dir
from .scene import Scene


FLAG_WINDOWED = 0
FLAG_MINIMIZED = 1
FLAG_MAXIMIZED = 2
FLAG_FULLSCREEN = 3
FLAG_FULLSCREEN_DESKTOP = 4


class Window:
    def __init__(
        self, title: str, size: tuple, pos: tuple, mode: int,
        opacity: float, utility: bool
    ):
        self.window = pygame.Window(title, size, pos, )
    
    def run_scene(self, scene: "Scene"):
        pass
    
    def update(self):
        pass
    
    def close(self):
        pass
