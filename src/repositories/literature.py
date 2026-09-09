from __future__ import annotations

from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from ..tools.literature import Evidence, Paper


class LiteratureRepository(Protocol):
    def search_papers(self, query: str, limit: int = 10) -> list[Paper]:
        ...

    def retrieve_evidence(self, paper_id: str) -> list[Evidence]:
        ...


_repository: LiteratureRepository | None = None


def configure_literature_repository(repository: LiteratureRepository) -> None:
    global _repository
    _repository = repository


def get_literature_repository() -> LiteratureRepository:
    if _repository is None:
        raise RuntimeError("Literature repository has not been configured")
    return _repository

