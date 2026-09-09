from mcp import mcp
from pydantic import BaseModel

from ..repositories.literature import get_literature_repository


class Paper(BaseModel):
    """A scientific paper."""

    id: str
    title: str
    authors: list[str]
    abstract: str
    journal: str
    year: int
    doi: str


class Evidence(BaseModel):
    """Evidence extracted from a paper."""

    paper_id: str
    evidence_text: str
    confidence_score: float


@mcp.tool()
def search_papers(query: str, limit: int = 10) -> list[Paper]:
    """Search for scientific papers based on a query."""
    return get_literature_repository().search_papers(query, limit)


@mcp.tool()
def retrieve_evidence(paper_id: str) -> list[Evidence]:
    """Retrieve evidence from a specific paper based on its ID."""
    return get_literature_repository().retrieve_evidence(paper_id)

