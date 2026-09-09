from __future__ import annotations

from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from ..tools.compounds import Compound


class CompoundRepository(Protocol):
    def search_compounds(self, query: str, limit: int = 10) -> list[Compound]:
        ...


_repository: CompoundRepository | None = None


def configure_compound_repository(repository: CompoundRepository) -> None:
    global _repository
    _repository = repository


def get_compound_repository() -> CompoundRepository:
    if _repository is None:
        raise RuntimeError("Compound repository has not been configured")
    return _repository

