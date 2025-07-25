# devhands/domain/interfaces/app_action_interface.py

from abc import ABC, abstractmethod


class AppActionInterface(ABC):
    """Interface for an app action (e.g., building a new app or analyzing an existing one)."""

    @abstractmethod
    def run(self) -> None:
        """Executes the action."""
        pass
