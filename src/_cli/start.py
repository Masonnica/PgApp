from pathlib import Path


config = """[application]
name = "<your app name>"
description = "<your app description>"
version = "<your app version>"
main_scene = "scenes/main.pgasc"

[display]
viewport_width = 800
viewport_height = 600
mode = "windowed"
"""

main = """import pgapp

pgapp.init()
pgapp.run()
"""

main_scene = """
"""


def run():
    target_dir = Path.cwd()
    
    print(f"Khởi tạo dự án mới tại: {target_dir}")
    
    print("  Tạo file: \t\t\tconfig.toml")
    config_path = Path(f"{target_dir}/config.toml")
    config_path.touch()
    config_path.write_text(config, encoding="utf-8")
    del config_path
    
    print("  Tạo file: \t\t\tmain.py")
    main_path = Path(f"{target_dir}/main.py")
    main_path.touch()
    main_path.write_text(main, encoding="utf-8")
    del main_path
    
    print("  Tạo thư mục: \t\t\tassets")
    (target_dir/"assets").mkdir(parents=True, exist_ok=True)
    
    print("    Tạo thư mục: \t\timgs")
    (target_dir/"assets"/"imgs").mkdir(parents=True, exist_ok=True)
    
    print("    Tạo thư mục: \t\tfonts")
    (target_dir/"assets"/"fonts").mkdir(parents=True, exist_ok=True)
    
    print("    Tạo thư mục: \t\tsounds")
    (target_dir/"assets"/"sounds").mkdir(parents=True, exist_ok=True)
    
    print("  Tạo thư mục: \t\t\tscenes")
    (target_dir/"scenes").mkdir(parents=True, exist_ok=True)
    
    print("    Tạo file: \t\t\tmain.pgasc")
    main_path = Path(f"{target_dir}/scenes/main.pgasc")
    main_path.touch()
    main_path.write_text(main, encoding="utf-8")
    del main_path
    
    print("  Tạo thư mục: \t\t\tscripts")
    (target_dir/"scripts").mkdir(parents=True, exist_ok=True)
