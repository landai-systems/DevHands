# tests/core/test_new_app_builder.py

import shutil
from pathlib import Path
from devhands.core.new_app_builder import NewAppBuilder


def test_create_project_structure(tmp_path: Path):
    builder = NewAppBuilder()
    test_dir = tmp_path / "testapp"

    builder._create_project_structure(test_dir)

    # Check directory structure
    assert (test_dir / "app").exists()
    assert (test_dir / "tests").exists()
    assert (test_dir / "docker").exists()

    # Check README file
    readme = test_dir / "README.md"
    assert readme.exists()
    assert readme.read_text().startswith("# testapp")
