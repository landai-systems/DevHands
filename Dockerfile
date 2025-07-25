# Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System dependencies for Poetry & build
RUN apt-get update && apt-get install -y curl build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    rm -rf /var/lib/apt/lists/*

# Add Poetry to environment PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy only lock & toml to optimize image layers
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy app code
COPY . .

# Startup command
CMD ["poetry", "run", "python", "devhands/main.py"]
