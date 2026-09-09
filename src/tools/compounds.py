from mcp import mcp
from pydantic import BaseModel
from typing import Protocol


class Compound(BaseModel):
    """A chemical compound."""

    id: str
    name: str
    formula: str
    molecular_weight: float


class CompoundRepository(Protocol):
    """Abstraction for the compound retrieval service."""

    def search_compounds(self, query: str, limit: int = 10) -> list[Compound]:
        ...


_repository: CompoundRepository | None = None


def configure_compound_repository(repository: CompoundRepository) -> None:
    """Configure the compound retrieval service."""
    global _repository
    _repository = repository


@mcp.tool()
def search_compounds(query: str, limit: int = 10) -> list[Compound]:
    """Search for chemical compounds based on a query."""
    if _repository is None:
        raise RuntimeError("Compound repository has not been configured")
    return _repository.search_compounds(query, limit)

