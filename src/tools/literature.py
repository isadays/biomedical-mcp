from mcp import mcp
from pydantic import BaseModel
from typing import Protocol


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


class LiteratureRepository(Protocol):
    """Abstraction for the literature retrieval service."""

    def search_papers(self, query: str, limit: int = 10) -> list[Paper]:
        ...

    def retrieve_evidence(self, paper_id: str) -> list[Evidence]:
        ...


_repository: LiteratureRepository | None = None


def configure_literature_repository(repository: LiteratureRepository) -> None:
    """Configure the literature retrieval service."""
    global _repository
    _repository = repository


@mcp.tool()
def search_papers(query: str, limit: int = 10) -> list[Paper]:
    """Search for scientific papers based on a query."""
    if _repository is None:
        raise RuntimeError("Literature repository has not been configured")
    return _repository.search_papers(query, limit)


@mcp.tool()
def retrieve_evidence(paper_id: str) -> list[Evidence]:
    """Retrieve evidence from a specific paper based on its ID."""
    if _repository is None:
        raise RuntimeError("Literature repository has not been configured")
    return _repository.retrieve_evidence(paper_id)

