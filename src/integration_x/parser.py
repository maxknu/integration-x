"""SOAP XML parser: ListCompaniesResponse → list[dict]."""

from __future__ import annotations

NS = {
    "soap": "http://schemas.xmlsoap.org/soap/envelope/",
    "tns": "http://soap-crm.local/services",
    "s0": "http://soap-crm.local/types",
}

FIELDS = [
    "Id",
    "Name",
    "OrgNumber",
    "Industry",
    "Website",
    "Phone",
    "Email",
    "Address",
    "City",
    "Country",
]


def parse_file(path: str) -> list[dict[str, str]]:
    """Parse a SOAP ListCompaniesResponse file into a list of raw record dicts.

    All field values are raw strings (or empty string when the element is absent).
    Raises ValueError on malformed XML or missing envelope structure.
    """
    raise NotImplementedError
