# tests/cli/test_menu.py

from devhands.cli.menu import Menu, UserChoice


class MockController:
    def __init__(self):
        self.called = ""

    def create_new_app(self):
        self.called = "new"

    def refactor_existing_app(self):
        self.called = "refactor"


def test_menu_new_app_selection(monkeypatch):
    controller = MockController()
    menu = Menu(controller)

    monkeypatch.setattr("builtins.input", lambda _: "1")
    menu.display()
    assert controller.called == "new"


def test_menu_refactor_selection(monkeypatch):
    controller = MockController()
    menu = Menu(controller)

    monkeypatch.setattr("builtins.input", lambda _: "2")
    menu.display()
    assert controller.called == "refactor"
