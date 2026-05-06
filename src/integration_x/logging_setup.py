"""Run-log buffer and token redaction utilities."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import ClassVar


class RunLog:
    """Collects structured log lines for a single integration run."""

    _SECRETS: ClassVar[list[str]] = []

    def __init__(self) -> None:
        self._lines: list[str] = []

    @classmethod
    def register_secret(cls, value: str) -> None:
        if value:
            cls._SECRETS.append(value)

    def _redact(self, text: str) -> str:
        for secret in self._SECRETS:
            text = text.replace(secret, "***")
        return text

    def _append(self, level: str, message: str) -> None:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        self._lines.append(f"{ts} {level:<5} {self._redact(message)}")

    def info(self, message: str) -> None:
        self._append("INFO", message)

    def warn(self, message: str) -> None:
        self._append("WARN", message)

    def error(self, message: str) -> None:
        self._append("ERROR", message)

    def flush_to_string(self) -> str:
        return "\n".join(self._lines)

    def flush_to_stdout(self) -> None:
        for line in self._lines:
            print(line)


def configure_stdlib_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)-5s %(name)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )
