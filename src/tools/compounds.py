from mcp import mcp
from pydantic import BaseModel

from ..repositories.compounds import get_compound_repository


class Compound(BaseModel):
    """A chemical compound."""

    id: str
    name: str
    formula: str
    molecular_weight: float


@mcp.tool()
def search_compounds(query: str, limit: int = 10) -> list[Compound]:
    """Search for chemical compounds based on a query."""
    return get_compound_repository().search_compounds(query, limit)

