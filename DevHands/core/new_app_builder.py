# devhands/core/new_app_builder.py

import os
from pathlib import Path
from devhands.domain.interfaces.app_action_interface import AppActionInterface


class NewAppBuilder(AppActionInterface):
    """
    Builds a new app project based on user-provided MVP details.
    Initially CLI-based (later: agentic prompt flow via LangChain).
    """

    def __init__(self) -> None:
        self.project_root: Path = Path.cwd() / "generated_apps"

    def run(self) -> None:
        """Starts the build flow for a new app."""
        print("\n🚀 Creating a new app.")
        app_name = input("Enter a name for the project: ").strip()

        if not app_name:
            print("❌ Project name cannot be empty.")
            return

        target_dir = self.project_root / app_name
        if target_dir.exists():
            print(f"❌ Project folder '{target_dir}' already exists.")
            return

        # Create structure
        self._create_project_structure(target_dir)
        print(f"✅ App '{app_name}' successfully created at: {target_dir}\n")

    def _create_project_structure(self, base_path: Path) -> None:
        """Generates the basic structure of the new project."""
        os.makedirs(base_path / "app", exist_ok=True)
        os.makedirs(base_path / "tests", exist_ok=True)
        os.makedirs(base_path / "docker", exist_ok=True)

        # Empty placeholder files
        (base_path / "README.md").write_text(f"# {base_path.name}\n\nGenerated with DevHands.")
        (base_path / "app" / "__init__.py").touch()
        (base_path / "tests" / "__init__.py").touch()
