from __future__ import annotations

from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from ..tools.relationships import Relationship


class RelationshipRepository(Protocol):
    def find_relationships(self, paper_ids: list[str]) -> list[Relationship]:
        ...


_repository: RelationshipRepository | None = None


def configure_relationship_repository(repository: RelationshipRepository) -> None:
    global _repository
    _repository = repository


def get_relationship_repository() -> RelationshipRepository:
    if _repository is None:
        raise RuntimeError("Relationship repository has not been configured")
    return _repository

