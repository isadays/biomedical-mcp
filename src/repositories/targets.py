from __future__ import annotations

from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from ..tools.targets import Target


class TargetRepository(Protocol):
    def search_targets(self, query: str, limit: int = 10) -> list[Target]:
        ...


_repository: TargetRepository | None = None


def configure_target_repository(repository: TargetRepository) -> None:
    global _repository
    _repository = repository


def get_target_repository() -> TargetRepository:
    if _repository is None:
        raise RuntimeError("Target repository has not been configured")
    return _repository

