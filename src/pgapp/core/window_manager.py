from .window import Window

class WindowManager:
    def __init__(self):
        self.windows = {}
    
    def new_window(self, id: str, title: str, size: tuple[int, int], flag: int):
        pass
    
    def close_window(self, id: str):
        pass
    
    def close_all_window(self):
        pass