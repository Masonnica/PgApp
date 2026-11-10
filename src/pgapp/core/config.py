import sys
import inspect
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


_CONFIG: None|dict = None
_ROOT_DIR: None|str = None


def print_error(prop: str, msg: str):
    print(f"\033[1;31mLỗi cấu hình:\033[0m\033[1m {prop}\033[0m - {msg}")

def set_up():
    caller_frame = inspect.stack()[2]
    caller_file = Path(caller_frame.filename).resolve()
    config_path = caller_file.parent / "config.toml"
    
    global _ROOT_DIR
    _ROOT_DIR = caller_file.parent
    
    if not config_path.exists():
        raise FileNotFoundError(
            f"Không tìm thấy file config: {config_path}. "
            f"Tạo file config.toml cùng thư mục với '{caller_file.name}' trước khi gọi pgapp.init()."
        )
    
    with open(config_path, "rb") as f:
        data = tomllib.load(f)
    
    print(data)
    
    Config(data)

def get_config():
    return _CONFIG

def get_root_dir():
    return _ROOT_DIR


class Config:
    def __init__(self, config: dict):
        self.root_dir = _ROOT_DIR
        self.config = config
        
        check = True
        check = check and self._check_app_prop()
        check = check and self._check_dis_prop()
        
        if not check:
            raise ValueError("Giá trị thuộc tính không hợp lệ hoặc không khả thi")
        
        global _CONFIG
        _CONFIG = self.config
        
        del self
    
    def _check_app_prop(self) -> bool:
        check = True
        props = self.config["application"]
        
        if not type(props["name"]) is str:
            check = False
            print_error("name", "không đúng kiểu dữ liệu (string)")
        if not type(props["description"]) is str:
            check = False
            print_error("description", "không đúng kiểu dữ liệu (string)")
        if not type(props["version"]) is str:
            check = False
            print_error("version", "không đúng kiểu dữ liệu (string)")
        if not type(props["main_scene"]) is str:
            check = False
            print_error("main_scene", "không đúng kiểu dữ liệu (string)")
        elif not (self.root_dir/props["main_scene"]).exists():
            check = False
            print_error("main_scene", f"tệp {"<root>/" + props["main_scene"]} không tồn tại")
        
        return check
    
    def _check_dis_prop(self) -> bool:
        check = True
        props = self.config["display"]
        
        if not type(props["window_size"]) is dict:
            check = False
            print_error("window_size", "không đúng kiểu dữ liệu (dictionary)")
        elif not type(props["window_size"]["x"]) is int:
            check = False
            print_error("window_size.x", "không đúng kiểu dữ liệu (integer)")
        elif not type(props["window_size"]["y"]) is int:
            check = False
            print_error("window_size.y", "không đúng kiểu dữ liệu (integer)")
        
        if not type(props["window_pos"]) is dict:
            check = False
            print_error("window_pos", "không đúng kiểu dữ liệu (dictionary)")
        elif not type(props["window_pos"]["x"]) is int:
            check = False
            print_error("window_pos.x", "không đúng kiểu dữ liệu (integer)")
        elif not type(props["window_pos"]["y"]) is int:
            check = False
            print_error("window_pos.y", "không đúng kiểu dữ liệu (integer)")
        
        if not type(props["mode"]) is str:
            check = False
            print_error("mode", "không đúng kiểu dữ liệu (string)")
        elif props["mode"] not in ["windowed", "minimized", "maximized", "fullscreen", "fullscreen_desktop"]:
            check = False
            print_error("mode", "giá trị nằm ngoài tùy chọn ('windowed', 'minimized', 'maximized', 'fullscreen', 'fullscreen_desktop')")
        
        if not type(props["opacity"]) is float:
            check = False
            print_error("opacity", "không đúng kiểu dữ liệu (float)")
        
        if not type(props["utility"]) is bool:
            check = False
            print_error("utility", "không đúng kiểu dữ liệu (boolean)")
        
        return check
