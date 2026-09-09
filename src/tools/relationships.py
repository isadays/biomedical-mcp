from mcp import mcp
from pydantic import BaseModel
from typing import Protocol


class Relationship(BaseModel):
    """A relationship between two papers."""

    source_id: str
    relationship: str
    target_id: str


class RelationshipRepository(Protocol):
    """Abstraction for the paper relationship retrieval service."""

    def find_relationships(self, paper_ids: list[str]) -> list[Relationship]:
        ...


_repository: RelationshipRepository | None = None


def configure_relationship_repository(repository: RelationshipRepository) -> None:
    """Configure the paper relationship retrieval service."""
    global _repository
    _repository = repository


@mcp.tool()
def find_relationships(paper_ids: list[str]) -> list[Relationship]:
    """Find relationships between papers based on their IDs."""
    if _repository is None:
        raise RuntimeError("Relationship repository has not been configured")
    return _repository.find_relationships(paper_ids)

