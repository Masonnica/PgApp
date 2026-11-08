import pygame
from pathlib import Path

from .config import get_config, get_root_dir
from .window import Window
from .scene import Scene

class App:
    def __init__(self):
        pygame.init()
        main_scene = Scene(Path(f"{get_root_dir()}/{get_config()["application"]["main_scene"]}"))
        self.main_window = Window(get_config()["application"]["name"], main_scene)
    
    def run(self) -> None:
        pass
