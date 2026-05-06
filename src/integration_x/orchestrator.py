"""Orchestrator: drives the end-to-end run for a single integration pass."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from integration_x.config import Config


def run(config: "Config", *, dry_run: bool = False) -> int:
    """Execute one full pass: list → download → parse → normalize → upsert → archive → log.

    Returns 0 on success (per-row skips are not failures), 1 if any file
    failed at the parse/archive/log-upload step.
    """
    raise NotImplementedError
