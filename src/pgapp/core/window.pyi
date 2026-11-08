from .scene import Scene

FLAG_WINDOWED: int
FLAG_MINIMIZED: int
FLAG_MAXIMIZED: int
FLAG_FULLSCREEN: int

class Window:
    def __init__(self, title: str, scene: "Scene"): ...
