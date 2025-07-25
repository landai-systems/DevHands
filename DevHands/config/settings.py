# devhands/config/settings.py

"""
Environment-based configuration settings for DevHands.
Loads secrets and environment variables using dotenv.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# === OpenAI & LangChain ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "devhands")

# === LLM Settings ===
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.3"))

# === Logging & Environment ===
LOG_LEVEL = os.getenv("DEVHANDS_LOG_LEVEL", "INFO")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
