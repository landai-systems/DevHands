# devhands/infrastructure/tools/diff_generator.py

from pathlib import Path
from devhands.infrastructure.tools.langchain_agent import LangchainAgent


class DiffGenerator:
    """
    Performs an AI-based analysis and returns code improvement suggestions in diff format.
    """

    def __init__(self, agent: LangchainAgent) -> None:
        self.agent = agent

    def analyze_file(self, file_path: Path, goal: str = "Improvement based on SOLID principles") -> str:
        """
        Reads the file content and analyzes it using the LLM.
        Returns a suggestion in diff-like format.
        """
        if not file_path.exists() or not file_path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")

        code = file_path.read_text(encoding="utf-8")
        if not code.strip():
            return f"# File {file_path.name} is empty. No refactoring needed."

        print(f"🧠 Analyzing file: {file_path.name} ...")
        response = self.agent.explain_code(code, goal)
        return response
