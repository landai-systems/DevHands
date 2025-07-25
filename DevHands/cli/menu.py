# devhands/cli/menu.py

from enum import Enum
from devhands.core.app_controller import AppController


class UserChoice(str, Enum):
    NEW_APP = "1"
    REFACTOR_APP = "2"
    EXIT = "0"


class Menu:
    def __init__(self, controller: AppController) -> None:
        self.controller = controller

    def display(self) -> None:
        print("👋 Welcome to DevHands – your AI Development Partner.\n")
        print("What would you like to do?")
        print("[1] Create a new app")
        print("[2] Analyze & improve an existing app")
        print("[0] Exit")

        choice = input("\nPlease choose an option: ").strip()

        if choice == UserChoice.NEW_APP:
            self.controller.create_new_app()
        elif choice == UserChoice.REFACTOR_APP:
            self.controller.refactor_existing_app()
        elif choice == UserChoice.EXIT:
            print("👋 Goodbye!")
        else:
            print("❌ Invalid selection. Please try again.")
            self.display()
