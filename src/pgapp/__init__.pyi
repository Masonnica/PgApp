from .core.app import App
from .core.window import Window
from .core.scene import Scene
from .core.widget import Widget

__version__: str
__all__: list[str]

def init() -> None: ...
def run(scene: "Scene") -> None: ...