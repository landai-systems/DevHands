# devhands/infrastructure/docker/builder.py

from pathlib import Path


class DockerBuilder:
    """
    Creates a Dockerfile and optionally a docker-compose.yml for an app project.
    """

    def __init__(self, app_dir: Path) -> None:
        self.app_dir = app_dir.resolve()
        self.dockerfile_path = self.app_dir / "Dockerfile"
        self.compose_path = self.app_dir / "docker-compose.yml"

    def generate_dockerfile(self) -> None:
        """Generates a simple, secure Dockerfile for a Python app."""
        content = """# syntax=docker/dockerfile:1
            FROM python:3.11-slim

            ENV PYTHONDONTWRITEBYTECODE=1
            ENV PYTHONUNBUFFERED=1

            WORKDIR /app
            COPY . /app

            RUN pip install --no-cache-dir --upgrade pip && \\
                pip install -r requirements.txt

            CMD ["python", "main.py"]
            """
        self.dockerfile_path.write_text(content.strip(), encoding="utf-8")
        print(f"✅ Dockerfile created at: {self.dockerfile_path}")

    def generate_compose_file(self) -> None:
        """Optional: Generates a docker-compose.yml with minimal configuration."""
        content = f"""version: '3.8'
            services:
            app:
                build: .
                container_name: {self.app_dir.name}_container
                volumes:
                - .:/app
                ports:
                - "8000:8000"
                command: python main.py
            """
        self.compose_path.write_text(content.strip(), encoding="utf-8")
        print(f"✅ docker-compose.yml created at: {self.compose_path}")
