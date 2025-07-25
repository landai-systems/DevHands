# devhands/core/app_analyzer.py

import os
from pathlib import Path
from typing import List

from devhands.domain.interfaces.app_action_interface import AppActionInterface


class AppAnalyzer(AppActionInterface):
    """
    Analyzes an existing app and prepares a SOLID-based refactoring recommendation.
    Will later delegate to an LLM-powered DiffGenerator.
    """

    IGNORED_FILENAMES = {
        ".gitignore", ".env", ".dockerignore", "requirements.txt",
        "pyproject.toml", "Dockerfile", "docker-compose.yml"
    }

    def __init__(self) -> None:
        self.target_path: Path | None = None

    def run(self) -> None:
        print("\n🔍 Analyze & improve existing app")

        input_path = input("Enter the path to the existing project folder: ").strip()
        path = Path(input_path).resolve()

        if not path.exists() or not path.is_dir():
            print(f"❌ Path '{path}' is invalid or does not exist.")
            return

        self.target_path = path
        files = self._collect_relevant_files(path)

        if not files:
            print("⚠️ No relevant files found.")
            return

        print(f"✅ Found {len(files)} relevant files.")
        for f in files:
            print(f" - {f.relative_to(path)}")

        # TODO: Pass to LLM-powered DiffTool
        print("\n🧠 Preparation for refactor analysis completed.\n")

    def _collect_relevant_files(self, root: Path) -> List[Path]:
        """Collects relevant code files, ignoring irrelevant or nearly empty ones."""
        relevant = []
        for file in root.rglob("*"):
            if file.is_file() and file.suffix in {".py", ".tsx", ".ts", ".js", ".jsx"}:
                if file.name in self.IGNORED_FILENAMES:
                    continue
                if file.stat().st_size < 20:  # < 20 bytes = empty or nearly empty
                    continue
                relevant.append(file)
        return relevant
