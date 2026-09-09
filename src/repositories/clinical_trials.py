from __future__ import annotations

from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from ..tools.clinical_trials import ClinicalTrial


class ClinicalTrialRepository(Protocol):
    def search_clinical_trials(self, query: str, limit: int = 10) -> list[ClinicalTrial]:
        ...


_repository: ClinicalTrialRepository | None = None


def configure_clinical_trial_repository(repository: ClinicalTrialRepository) -> None:
    global _repository
    _repository = repository


def get_clinical_trial_repository() -> ClinicalTrialRepository:
    if _repository is None:
        raise RuntimeError("Clinical-trial repository has not been configured")
    return _repository

