import os

BASE_DIR = "DevHands"

# Strukturdefinition: Ordner → Dateien
structure = {
    ".": [
        "README.md",
        ".gitignore",
        ".env.example",
        "Dockerfile",
        "docker-compose.yml",
        "Makefile",
        "pyproject.toml"
    ],
    "scripts": [
        "start.sh",
        "test.sh",
        "lint.sh"
    ],
    "ci": [
        "github.yml"
    ],
    f"{BASE_DIR}": [
        "__init__.py"
    ],
    f"{BASE_DIR}/cli": [
        "__init__.py",
        "menu.py"
    ],
    f"{BASE_DIR}/config": [
        "settings.py"
    ],
    f"{BASE_DIR}/core": [
        "agent_factory.py",
        "app_analyzer.py",
        "new_app_builder.py",
        "prompt_manager.py",
        "docker_packager.py"
    ],
    f"{BASE_DIR}/domain/interfaces": [
        "tool_interface.py",
        "file_parser_interface.py",
        "memory_interface.py"
    ],
    f"{BASE_DIR}/domain/models": [
        "mvp_spec.py",
        "file_metadata.py"
    ],
    f"{BASE_DIR}/infrastructure/tools": [
        "langchain_agent.py",
        "file_parser.py",
        "diff_generator.py"
    ],
    f"{BASE_DIR}/infrastructure/memory": [
        "memory_langchain.py",
        "memory_inmemory.py"
    ],
    f"{BASE_DIR}/infrastructure/docker": [
        "builder.py"
    ],
    "tests/core": [],
    "tests/cli": [],
    "tests/infrastructure": [],
    "tests": [
        "conftest.py"
    ]
}

# Standardinhalte für bestimmte Dateien
file_contents = {
    "README.md": "# DevHands\n\nAgentic AI CLI Tool to create or refactor apps using LangChain.",
    ".gitignore": """# Python
__pycache__/
*.pyc
*.pyo
*.pyd
env/
venv/
*.env

# VS Code
.vscode/

# Docker
*.log
*.pid
docker-compose.override.yml
.devcontainer/

# LangChain
lc_logs/
    """,
    "pyproject.toml": """[tool.poetry]
name = "DevHands"
version = "0.1.0"
description = "Agentic AI CLI Tool with LangChain"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
langchain = "*"
click = "*"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
    """,
    "Dockerfile": """FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install poetry && poetry install
CMD ["poetry", "run", "python", "-m", "DevHands.main"]
    """,
    "docker-compose.yml": """version: '3.8'
services:
  DevHands:
    build: .
    volumes:
      - .:/app
    command: poetry run python -m DevHands.main
    """,
    "Makefile": """run:
\tpoetry run python -m DevHands.main

test:
\tpytest
    """,
    f"{BASE_DIR}/__init__.py": '"""DevHands root module."""',
    f"{BASE_DIR}/config/settings.py": "# Configuration settings"
}

def create_structure():
    for folder, files in structure.items():
        dir_path = os.path.join(folder)
        os.makedirs(dir_path, exist_ok=True)
        print(f"[✓] Created folder: {dir_path}")
        for file in files:
            file_path = os.path.join(dir_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    content = file_contents.get(file_path, "")
                    f.write(content)
                print(f"    └── Created file: {file_path}")

if __name__ == "__main__":
    print("🔧 Creating DevHands project structure...")
    create_structure()
    print("\n✅ Done. Your project scaffold is ready.")
