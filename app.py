import colorama
import load_config
import sys
import func


def print_help():
    print("""
    FocusThis

    Usage:
        focis [OPTIONS]

    Options:
        -h, --help              Show this help message and exit.
        -v, --version           Show program's version number and exit.

    Examples:
        q                       Quit the application
        focis                   Run FocusThis
        focis --help            Show help
        focis --version         Show version
    """)

class SimpleTileApp():

    def run(self):
            func.main()

    def main_function(self):
        print(text_txt)


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            print_help()
            return
        elif sys.argv[1] == "--version":
            print("SimpleTileApp v0.1.0")
            return
        else:
            print(f"Неизвестный аргумент: {sys.argv[1]}")
            print("Используйте --help для получения справки")
            return

    app = SimpleTileApp()
    app.run()


if __name__ == "__main__":
    main()
