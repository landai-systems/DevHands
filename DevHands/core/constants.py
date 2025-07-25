# devhands/core/constants.py

from enum import Enum


class ProjectType(str, Enum):
    """Possible types of projects."""
    NEW = "new"
    REFACTOR = "refactor"


class AppStructure(str, Enum):
    """Supported app structures for new projects."""
    FASTAPI = "fastapi"
    FLASK = "flask"
    DJANGO = "django"
    REACT = "react"
    FULLSTACK = "fullstack"


class OutputFormat(str, Enum):
    """Formats for output and further processing."""
    TEXT = "text"
    JSON = "json"
    MARKDOWN = "markdown"
    DIFF = "diff"
