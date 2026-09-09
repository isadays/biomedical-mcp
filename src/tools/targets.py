from mcp import mcp
from pydantic import BaseModel
from typing import Protocol


class Target(BaseModel):
    """A biological target."""

    id: str
    name: str
    type: str


class TargetRepository(Protocol):
    """Abstraction for the biological target retrieval service."""

    def search_targets(self, query: str, limit: int = 10) -> list[Target]:
        ...


_repository: TargetRepository | None = None


def configure_target_repository(repository: TargetRepository) -> None:
    """Configure the biological target retrieval service."""
    global _repository
    _repository = repository


@mcp.tool()
def search_targets(query: str, limit: int = 10) -> list[Target]:
    """Search for biological targets based on a query."""
    if _repository is None:
        raise RuntimeError("Target repository has not been configured")
    return _repository.search_targets(query, limit)

