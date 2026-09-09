from mcp import mcp
from pydantic import BaseModel

from ..repositories.relationships import get_relationship_repository


class Relationship(BaseModel):
    """A relationship between two papers."""

    source_id: str
    relationship: str
    target_id: str


@mcp.tool()
def find_relationships(paper_ids: list[str]) -> list[Relationship]:
    """Find relationships between papers based on their IDs."""
    return get_relationship_repository().find_relationships(paper_ids)

