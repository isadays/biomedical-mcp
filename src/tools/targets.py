"""Biological target search MCP tool."""

from typing import Protocol

from mcp import mcp
from pydantic import BaseModel


class Target(BaseModel):
    id: str
    name: str
    type: str


class TargetRepository(Protocol):
    def search(self, query: str, limit: int) -> list[Target]: ...




@mcp.tool()
def search_targets(query: str, limit: int = 10) -> list[Target]:
    """Search biological targets by identifier, name, or target type."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 100:
        raise ValueError("limit must be an integer between 1 and 100")
    return _repository.search(query.strip(), limit)

