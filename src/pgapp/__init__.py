import os
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

from .core.app import App
from .core.window import Window
from .core.scene import Scene
from .core.node import Node

from .core import config

__version__ = "0.0.1"
__all__ = [
    "App",
    "Window",
    "Scene",
    "Node",
    "init",
    "run",
]

def init() -> None:
    """Chỉ gọi pgapp.init() ở tệp khởi đầu của chương trình và tệp đó phải ở cùng cấp thư mục với tệp config.toml."""
    config.set_up()

def run() -> None:
    """Hàm khởi chạy chương trình."""
    app = App()
    app.run()
