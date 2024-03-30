from typing import Dict, Optional

from detectors.detector import IDetector


class TeamNameDetector(IDetector):
    """
    detects the creation of teams with suspicious names (by the name prefix)
    """
    def __init__(self, prefix: str = "hacker"):
        self._prefix = prefix

    def detect(self, event_data: Dict) -> Optional[str]:
        team_name: str = event_data.get("team", {}).get("name")
        action_type = event_data.get("action")
        if not action_type or not team_name:
            raise ValueError("missing one of the parameters: action_type, team_name")
        if action_type == "created" and team_name.startswith(self._prefix):
            return (f"a team was created with the name '{team_name}' that starts with the suspicious prefix "
                    f"'{self._prefix}'")
