"""Compound search MCP tool."""

from mcp import mcp
from pydantic import BaseModel


class Compound(BaseModel):
    id: str
    name: str
    formula: str
    molecular_weight: float


class CompoundRepository(Protocol):
    def search(self, query: str, limit: int) -> list[Compound]: ...



@mcp.tool()
def search_compounds(query: str, limit: int = 10) -> list[Compound]:
    """Search compounds by identifier, name, or molecular formula."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string")
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 100:
        raise ValueError("limit must be an integer between 1 and 100")
    return _repository.search(query.strip(), limit)

