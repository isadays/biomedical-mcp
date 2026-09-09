from mcp import mcp
from pydantic import BaseModel

from ..repositories.targets import get_target_repository


class Target(BaseModel):
    """A biological target."""

    id: str
    name: str
    type: str


@mcp.tool()
def search_targets(query: str, limit: int = 10) -> list[Target]:
    """Search for biological targets based on a query."""
    return get_target_repository().search_targets(query, limit)

