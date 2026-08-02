import os
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")

from .core.app import App
from .core.window import Window
from .core.scene import Scene
from .core.widget import Widget

__version__ = "0.0.0"
__all__ = [
    "App",
    "Window",
    "Scene",
    "Widget",
    "init",
    "run",
]

def init() -> None:
    """Chỉ gọi pgapp.init() ở file khởi đầu của chương trình và phải có file cùng cấp config.toml."""
    import sys
    import inspect
    from pathlib import Path
    
    if sys.version_info >= (3, 11):
        import tomllib
    else:
        import tomli as tomllib
    
    if not os.environ.get("PGAPP_HIDE_SUPPORT_PROMPT"):
        print(f"Welcom to PgApp {__version__}!")
    
    caller_frame = inspect.stack()[1]
    caller_file = Path(caller_frame.filename).resolve()
    config_path = caller_file.parent / "config.toml"
    
    if not config_path.exists():
        raise FileNotFoundError(
			f"Không tìm thấy file config: {config_path}. "
			f"Tạo file config.toml cùng thư mục với '{caller_file.name}' trước khi gọi pgapp.init()."
		)
    
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    
    print(data)
    

def run() -> None:
    """Hàm khởi chạy ứng dụng."""
    pass
