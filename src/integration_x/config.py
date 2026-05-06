"""Environment-variable config loading and validation."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    sftp_host: str
    sftp_port: int
    sftp_username: str
    sftp_password: str
    sftp_inbox: str
    twenty_base_url: str
    twenty_api_token: str
    timeout_seconds: int
    log_level: str


def load_config() -> Config:
    """Read required env vars and return a validated Config.

    Raises SystemExit on missing or malformed values so the CLI can
    fail fast before any I/O.
    """
    port_str = _require("SFTP_PORT")
    try:
        port = int(port_str)
    except ValueError:
        raise SystemExit(f"SFTP_PORT must be an integer, got: {port_str!r}")

    timeout_str = os.environ.get("INTEGRATION_X_TIMEOUT_SECONDS", "30").strip() or "30"
    try:
        timeout = int(timeout_str)
    except ValueError:
        raise SystemExit(
            f"INTEGRATION_X_TIMEOUT_SECONDS must be an integer, got: {timeout_str!r}"
        )

    return Config(
        sftp_host=_require("SFTP_HOST"),
        sftp_port=port,
        sftp_username=_require("SFTP_USERNAME"),
        sftp_password=_require("SFTP_PASSWORD"),
        sftp_inbox=_require("SFTP_INBOX"),
        twenty_base_url=_require("TWENTY_BASE_URL"),
        twenty_api_token=_require("TWENTY_API_TOKEN"),
        timeout_seconds=timeout,
        log_level=os.environ.get("INTEGRATION_X_LOG_LEVEL", "INFO").strip().upper() or "INFO",
    )


def _require(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value
