"""Relationship discovery MCP tool."""


from mcp import mcp
from pydantic import BaseModel


class Relationship(BaseModel):
    source_id: str
    relationship: str
    target_id: str


class RelationshipRepository(Protocol):
    def find(self, paper_ids: Sequence[str]) -> list[Relationship]: ...





@mcp.tool()
def find_relationships(paper_ids: list[str]) -> list[Relationship]:
    """Find known relationships among the supplied paper identifiers."""
    if not isinstance(paper_ids, list) or not paper_ids:
        raise ValueError("paper_ids must be a non-empty list")
    if any(not isinstance(paper_id, str) or not paper_id.strip() for paper_id in paper_ids):
        raise ValueError("paper_ids must contain non-empty strings")
    return _repository.find(list(dict.fromkeys(paper_ids)))

