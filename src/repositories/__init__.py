"""Repository abstractions for biomedical data sources."""

from .clinical_trials import configure_clinical_trial_repository
from .compounds import configure_compound_repository
from .literature import configure_literature_repository
from .relationships import configure_relationship_repository
from .targets import configure_target_repository

__all__ = [
    "configure_clinical_trial_repository",
    "configure_compound_repository",
    "configure_literature_repository",
    "configure_relationship_repository",
    "configure_target_repository",
]
