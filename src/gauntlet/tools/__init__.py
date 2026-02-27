"""
gauntlet.tools - Third-party red team tool integrations.

Provides adapters for PyRIT (Microsoft), DeepTeam (Confident AI), and
Garak (NVIDIA) that convert tool-specific outputs into the package's
existing TestResult / AttackScenario data model.

Usage:
    from gauntlet.tools import ToolManager
    tm = ToolManager()
    print(tm.list_tools())
"""

from gauntlet.tools.base import RedTeamToolAdapter  # noqa: F401
from gauntlet.tools.tool_manager import ToolManager  # noqa: F401


def available_tools():
    """Quick helper that returns a list of detected tools and their status."""
    return ToolManager().list_tools()


__all__ = [
    "RedTeamToolAdapter",
    "ToolManager",
    "available_tools",
]
