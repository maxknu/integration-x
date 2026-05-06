"""Polars normaliser: raw record dicts → clean DataFrame."""

from __future__ import annotations

import polars as pl

SCHEMA: dict[str, pl.DataType] = {
    "id": pl.Utf8,
    "name": pl.Utf8,
    "org_number": pl.Utf8,
    "industry": pl.Utf8,
    "website": pl.Utf8,
    "phone": pl.Utf8,
    "email": pl.Utf8,
    "address_street1": pl.Utf8,
    "address_city": pl.Utf8,
    "address_country": pl.Utf8,
}


def normalize(records: list[dict[str, str]]) -> pl.DataFrame:
    """Convert raw parser output to a cleaned, deduped Polars DataFrame.

    Steps applied (all declarative):
    - Rename XML field keys to snake_case column names.
    - Trim whitespace on all string columns.
    - Normalise empty strings to null.
    - Lowercase website (scheme + host).
    - Drop rows where name is null.
    - Deduplicate on normalised name, keeping first occurrence.
    """
    raise NotImplementedError
