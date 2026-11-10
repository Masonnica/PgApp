from pathlib import Path
import time


config = """[application]
name = "<your app name>"
description = "<your app description>"
version = "<your app version>"
main_scene = "scenes/main.pgasc"

[display]
window_size = {"x" = 800, "y" = 600}
window_pos = {"x" = 0, "y" = 0}
mode = "windowed"
opacity = 1.0
utility = false
"""

main = """import pgapp

pgapp.init()
pgapp.run()
"""

main_scene = """
"""

main_script = """
"""

tree = {
    "folders": {
        "assets": {
            "folders": {
                "fonts": {},
                "images": {},
                "sounds": {},
            },
        },
        "scenes": {
            "files": {
                "main.pgasc": main_scene,
            },
        },
        "scripts": {
            "files": {
                "main.pgasr": main_script,
            },
        },
    },
    "files": {
        "config.toml": config,
        "main.py": main,
    },
}


def render_tree(dir: Path, tree: dict, level: int = 1):
    try:
        folders = list(tree["folders"].keys())
        for i in range(len(folders)):
            (dir/folders[i]).mkdir(parents=True, exist_ok=True)
            
            if i == len(folders) - 1 and not "files" in tree:
                print(f"{(' │  ' * (level - 1) + ' └──' + folders[i]):<32}\033[1;34m(folder)\033[0m")
            else:
                print(f"{(' │  ' * (level - 1) + ' ├──' + folders[i]):<32}\033[1;34m(folder)\033[0m")
            
            time.sleep(0.05)
            
            if tree["folders"][folders[i]]:
                render_tree((dir/folders[i]), tree["folders"][folders[i]], level + 1)
    except:
        pass
    
    try:
        files = list(tree["files"].keys())
        for i in range(len(files)):
            file_path = Path(dir/files[i])
            file_path.touch()
            file_path.write_text(tree["files"][files[i]], encoding="utf-8")
            
            if i == len(files) - 1:
                print(" │  " * (level - 1) + " └──" + files[i])
            else:
                print(" │  " * (level - 1) + " ├──" + files[i])
            
            time.sleep(0.05)
    except:
        pass

def run():
    target_dir = Path.cwd()
    
    print(f"Khởi tạo dự án mới tại: {target_dir}")
    
    render_tree(target_dir, tree)
