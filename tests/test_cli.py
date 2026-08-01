"""Smoke tests for the Step 1 command-line foundation."""

from pos_scraper import __version__
from pos_scraper.cli import build_environment_report, main


def test_environment_report_contains_expected_fields() -> None:
    report = build_environment_report()

    assert report["pos_scraper_version"] == __version__
    assert report["python_version"]
    assert report["python_executable"]
    assert report["platform"]
    assert report["working_directory"]


def test_doctor_command_returns_success(capsys) -> None:
    exit_code = main(["doctor"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "PosScraper environment check" in captured.out
    assert "Python Executable" in captured.out
