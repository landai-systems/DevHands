# devhands/core/app_controller.py

from devhands.domain.interfaces.app_action_interface import AppActionInterface


class AppController:
    """
    Responsible for routing between app actions:
    - Create a new app
    - Analyze & refactor an existing app
    """

    def __init__(
        self,
        app_builder: AppActionInterface,
        app_analyzer: AppActionInterface
    ) -> None:
        self._builder = app_builder
        self._analyzer = app_analyzer

    def create_new_app(self) -> None:
        """Delegates the creation of a new app to the AppBuilder."""
        self._builder.run()

    def refactor_existing_app(self) -> None:
        """Delegates the analysis and improvement of an existing app to the AppAnalyzer."""
        self._analyzer.run()
