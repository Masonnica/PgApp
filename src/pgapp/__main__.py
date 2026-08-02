import argparse
import importlib

class ColorHelpFormatter(argparse.HelpFormatter):
    USAGE_COLOR = "\033[1m"
    HEADING_COLOR = "\033[1;34m"
    ACTION_COLOR = "\033[36m"
    RESET = "_pgapp"
    
    def _format_usage(self, usage, actions, groups, prefix):
        text = super()._format_usage(usage, actions, groups, prefix="  ")
        return f"{self.HEADING_COLOR}\nUsage:{self.RESET}\n{self.USAGE_COLOR}{text}{self.RESET}"
    
    def start_section(self, heading):
        heading = f"{self.HEADING_COLOR}{heading}{self.RESET}"
        return super().start_section(heading)
    
    def _format_action_invocation(self, action):
        result = super()._format_action_invocation(action)
        return f"{self.ACTION_COLOR}{result}{self.RESET}"

def main():
    parser = argparse.ArgumentParser(
        prog="python -m pgapp",
        formatter_class=ColorHelpFormatter,
        add_help=False,
    )
    subparser = parser.add_subparsers(
        dest="cmd",
        title="Commands",
        metavar="<command>",
    )
    
    cmd_ver = subparser.add_parser("version", help="Hiện phiên bản của pgapp.")
    cmd_start = subparser.add_parser("start", help="Khởi tạo dự án mới với pgapp.")
    cmd_scene = subparser.add_parser("scene", help="Mở trình chỉnh sửa cảnh.")
    cmd_scene = subparser.add_parser("inputs", help="Mở trình chỉnh sửa bản đồ đầu vào.")
    cmd_theme = subparser.add_parser("theme", help="Mở trình chỉnh sửa chủ đề.")
    cmd_setting = subparser.add_parser("setting", help="Mở trình chỉnh sửa cài đặt.")
    cmd_scene = subparser.add_parser("help", help="Hiển thị cách dùng CLI và lệnh.")
    
    args = parser.parse_args()
    
    match args.cmd:
        case "version":
            importlib.import_module(f"_pgapp_cli.{"version"}")
        case "start":
            module = importlib.import_module("_pgapp_cli.start")
            module.run()
        case "scene":
            importlib.import_module(f"_pgapp_cli.{"scene"}")
        case "inputs":
            module = importlib.import_module("_pgapp_cli.input_map")
            module.run()
        case "theme":
            module = importlib.import_module("_pgapp_cli.theme")
            module.run()
        case "setting":
            module = importlib.import_module("_pgapp_cli.setting")
            module.run()
        case "help":
            parser.print_help()
            print()
        case None:
            parser.print_help()
            print()

if __name__ == "__main__":
    main()
