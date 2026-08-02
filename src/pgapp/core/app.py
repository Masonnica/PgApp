import pygame
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .scene import Scene

class App:
    def __init__(self):
        pygame.init()
    
    def run(self, scene: "Scene") -> None:
        pass
