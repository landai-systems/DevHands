# tests/core/test_app_analyzer.py

from pathlib import Path
from devhands.core.app_analyzer import AppAnalyzer


def test_collect_relevant_files_filters_irrelevant(tmp_path: Path):
    (tmp_path / ".env").write_text("SECRET=1")
    (tmp_path / "empty.py").write_text("")
    (tmp_path / "valid.py").write_text("print('hello')")
    (tmp_path / "valid.js").write_text("console.log('hi')")

    analyzer = AppAnalyzer()
    result = analyzer._collect_relevant_files(tmp_path)

    file_names = sorted([f.name for f in result])

    assert "valid.py" in file_names
    assert "valid.js" in file_names
    assert ".env" not in file_names
    assert "empty.py" not in file_names
