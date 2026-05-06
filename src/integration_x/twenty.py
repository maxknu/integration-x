"""Twenty CRM REST client: company lookup and creation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CompanyPayload:
    name: str
    domain_url: str | None = None
    address_street1: str | None = None
    address_city: str | None = None
    address_country: str | None = None


class TwentyClient:
    """Minimal REST client for Twenty CRM company operations."""

    def __init__(self, base_url: str, api_token: str, timeout: int = 30) -> None:
        self.base_url = base_url.rstrip("/")
        self._api_token = api_token
        self.timeout = timeout
        self._http: object | None = None

    def __enter__(self) -> "TwentyClient":
        self._build_client()
        return self

    def __exit__(self, *_: object) -> None:
        self._close_client()

    def _build_client(self) -> None:
        raise NotImplementedError

    def _close_client(self) -> None:
        raise NotImplementedError

    def company_exists(self, name: str) -> bool:
        """Return True if a non-deleted Company with this exact name exists."""
        raise NotImplementedError

    def create_company(self, payload: CompanyPayload) -> str:
        """POST a new Company; return the Twenty-assigned id."""
        raise NotImplementedError
