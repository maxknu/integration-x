"""CLI entry point: argument parsing and invocation of the run loop."""

from __future__ import annotations

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="integration-x",
        description="Pull SOAP XML from SFTP and upsert companies into Twenty CRM.",
    )
    p.add_argument(
        "--env-file",
        metavar="PATH",
        help="Path to .env file (default: ./.env).",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and normalise without writing to Twenty or archiving files.",
    )
    return p


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Load .env before importing config so vars are in the environment.
    _load_dotenv(args.env_file)

    from integration_x.config import load_config
    from integration_x.orchestrator import run

    config = load_config()
    sys.exit(run(config, dry_run=args.dry_run))


def _load_dotenv(env_file: str | None) -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    if env_file:
        load_dotenv(dotenv_path=env_file, override=False)
    else:
        load_dotenv(override=False)
