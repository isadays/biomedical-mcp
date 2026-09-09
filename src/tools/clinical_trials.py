"""Clinical-trial search MCP tool."""

from __future__ import annotations

from typing import Iterable, Protocol

from mcp import mcp

from pydantic import BaseModel


class ClinicalTrial(BaseModel):
    id: str
    title: str
    status: str
    phase: str
    conditions: list[str]
    interventions: list[str]
    locations: list[str]


class ClinicalTrialRepository(Protocol):
    def search(self, query: str, limit: int) -> list[ClinicalTrial]: ...




@mcp.tool()
def search_clinical_trials(query: str, limit: int = 10) -> list[ClinicalTrial]:
    """Search clinical trials by title, status, phase, condition, or intervention."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 100:
        raise ValueError("limit must be an integer between 1 and 100")
    return _repository.search(query.strip(), limit)

