"""SFTP client: list, download, move, and upload operations."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


class SFTPClient:
    """Thin wrapper around paramiko for inbox/processed/log operations."""

    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        inbox: str,
        timeout: int = 30,
    ) -> None:
        self.host = host
        self.port = port
        self.username = username
        self._password = password
        self.inbox = inbox
        self.timeout = timeout
        self._client: object | None = None
        self._sftp: object | None = None

    def connect(self) -> None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError

    def ensure_directories(self) -> None:
        """Create processed/ and log/ under inbox if absent."""
        raise NotImplementedError

    def list_xml_files(self) -> list[str]:
        """Return basenames of *.xml files in the inbox (non-recursive)."""
        raise NotImplementedError

    def download(self, remote_name: str, local_dir: Path) -> Path:
        """Download inbox/<remote_name> to local_dir; return local path."""
        raise NotImplementedError

    def move_to_processed(self, remote_name: str) -> str:
        """Move inbox/<remote_name> to inbox/processed/; return destination path."""
        raise NotImplementedError

    def upload_log(self, content: str, log_name: str) -> None:
        """Write content to inbox/log/<log_name> on the server."""
        raise NotImplementedError

    def __enter__(self) -> "SFTPClient":
        self.connect()
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
