from mcp import mcp
from pydantic import BaseModel

from ..repositories.clinical_trials import get_clinical_trial_repository


class ClinicalTrial(BaseModel):
    """A clinical trial."""

    id: str
    title: str
    status: str
    phase: str
    conditions: list[str]
    interventions: list[str]
    locations: list[str]


@mcp.tool()
def search_clinical_trials(query: str, limit: int = 10) -> list[ClinicalTrial]:
    """Search for clinical trials based on a query."""
    return get_clinical_trial_repository().search_clinical_trials(query, limit)

