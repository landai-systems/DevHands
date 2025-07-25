# devhands/main.py

from devhands.cli.menu import Menu
from devhands.core.app_controller import AppController
from devhands.core.new_app_builder import NewAppBuilder
from devhands.core.app_analyzer import AppAnalyzer


def main() -> None:
    """
    Entry point for DevHands.
    Initializes dependencies and starts the CLI menu.
    """
    builder = NewAppBuilder()
    analyzer = AppAnalyzer()
    controller = AppController(app_builder=builder, app_analyzer=analyzer)

    menu = Menu(controller)
    menu.display()


if __name__ == "__main__":
    main()
