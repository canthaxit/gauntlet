"""
gauntlet.core - Core red team engine components.
"""

import sys

from gauntlet.core.models import (
    DEFAULT_TARGET_URL,
    AttackCategory,
    AttackResult,
    AttackScenario,
    AttackTestResult,
    DifficultyLevel,
    TestResult,
)
from gauntlet.core.loader import ScenarioLoader
from gauntlet.core.executor import AttackExecutor
from gauntlet.core.evaluator import ResultEvaluator
from gauntlet.core.orchestrator import RedTeamOrchestrator
from gauntlet.core.metrics import pass_at_k, avg_turns_to_jailbreak, avg_risk_density


def _default_scenarios_path() -> str:
    """Resolve the path to the bundled default scenarios YAML."""
    if sys.version_info >= (3, 9):
        from importlib.resources import files
        return str(files("gauntlet") / "scenarios" / "default.yaml")
    import importlib.resources as _res
    with _res.path("gauntlet.scenarios", "default.yaml") as p:
        return str(p)


__all__ = [
    "DEFAULT_TARGET_URL",
    "AttackCategory",
    "AttackResult",
    "AttackScenario",
    "AttackTestResult",
    "DifficultyLevel",
    "TestResult",
    "ScenarioLoader",
    "AttackExecutor",
    "ResultEvaluator",
    "RedTeamOrchestrator",
    "pass_at_k",
    "avg_turns_to_jailbreak",
    "avg_risk_density",
    "_default_scenarios_path",
]
