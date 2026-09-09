from mcp import mcp
from pydantic import BaseModel
from typing import Protocol


class ClinicalTrial(BaseModel):
    """A clinical trial."""

    id: str
    title: str
    status: str
    phase: str
    conditions: list[str]
    interventions: list[str]
    locations: list[str]


class ClinicalTrialRepository(Protocol):
    """Abstraction for the clinical-trial retrieval service."""

    def search_clinical_trials(self, query: str, limit: int = 10) -> list[ClinicalTrial]:
        ...


_repository: ClinicalTrialRepository | None = None


def configure_clinical_trial_repository(repository: ClinicalTrialRepository) -> None:
    """Configure the clinical-trial retrieval service."""
    global _repository
    _repository = repository


@mcp.tool()
def search_clinical_trials(query: str, limit: int = 10) -> list[ClinicalTrial]:
    """Search for clinical trials based on a query."""
    if _repository is None:
        raise RuntimeError("Clinical-trial repository has not been configured")
    return _repository.search_clinical_trials(query, limit)

