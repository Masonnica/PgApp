import inspect
from pathlib import Path


_CONFIG: None|dict = None


def print_error(prop: str, msg: str):
    print(f"\033[1;31mLỗi:\033[0m\033[1m {prop}\033[0m - {msg}")


class Config:
    def __init__(self, config: dict):
        self.root_dir = Path(inspect.stack()[2].filename).resolve().parent
        self.config = config
        
        check = True
        check = check and self.check_app_prop()
        check = check and self.check_dis_prop()
        
        if not check:
            raise ValueError("Giá trị thuộc tính không hợp lệ hoặc không khả thi")
        
        global _CONFIG
        _CONFIG = self.config
    
    def check_app_prop(self) -> bool:
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
    
    def check_dis_prop(self) -> bool:
        check = True
        props = self.config["display"]
        
        if not type(props["viewport_width"]) is int:
            check = False
            print_error("viewport_width", "không đúng kiểu dữ liệu (integer)")
        if not type(props["viewport_height"]) is int:
            check = False
            print_error("viewport_height", "không đúng kiểu dữ liệu (integer)")
        if not type(props["mode"]) is str:
            check = False
            print_error("mode", "không đúng kiểu dữ liệu (string)")
        elif props["mode"] not in ["windowed", "minimized", "maximized", "fullscreen"]:
            check = False
            print_error("mode", "giá trị nằm ngoài tùy chọn ('windowed', 'minimized', 'maximized', 'fullscreen')")
        
        return check
