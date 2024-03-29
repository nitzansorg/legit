from typing import Dict, Optional, List

from detectors.detector import IDetector
from filters.action_type_filter import ActionTypeFilter
from filters.filter import IFilter


class TeamNameDetector(IDetector):
    """
    detects the creation of teams with suspicious names (by the name prefix)
    """
    def __init__(self, prefix: str = "hacker"):
        self._prefix = prefix

    def detect(self, event_data: Dict) -> Optional[str]:
        team_name: str = event_data["team"]["name"]
        action_type = event_data["action"]
        if action_type == "created" and team_name.startswith(self._prefix):
            return f"the team name '{team_name}' starts with the suspicious prefix '{self._prefix}'"
