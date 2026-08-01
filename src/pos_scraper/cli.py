"""Command-line entry point for PosScraper.

Step 1 intentionally provides only a small diagnostic command.  It verifies
that the repository has been cloned, the selected Python interpreter is active,
and the package can be imported before later steps add databases, scrapers, or
AI models.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path
from typing import Sequence

from pos_scraper import __version__


def build_environment_report() -> dict[str, str]:
    """Return useful, non-sensitive information about the active runtime."""

    return {
        "pos_scraper_version": __version__,
        "python_version": platform.python_version(),
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "working_directory": str(Path.cwd()),
    }


def create_parser() -> argparse.ArgumentParser:
    """Create the PosScraper command-line parser."""

    parser = argparse.ArgumentParser(
        prog="pos-scraper",
        description="PosScraper career opportunity intelligence system.",
    )
    subparsers = parser.add_subparsers(dest="command")

    doctor_parser = subparsers.add_parser(
        "doctor",
        help="Show the active Python environment and PosScraper installation.",
    )
    doctor_parser.add_argument(
        "--json",
        action="store_true",
        help="Print the environment report as JSON.",
    )

    return parser


def run_doctor(*, as_json: bool = False) -> int:
    """Print the environment report and return a process exit code."""

    report = build_environment_report()

    if as_json:
        print(json.dumps(report, indent=2))
        return 0

    print("PosScraper environment check")
    print("=" * 28)
    for key, value in report.items():
        readable_key = key.replace("_", " ").title()
        print(f"{readable_key}: {value}")

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run the PosScraper CLI."""

    parser = create_parser()
    args = parser.parse_args(argv)

    if args.command == "doctor":
        return run_doctor(as_json=args.json)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
