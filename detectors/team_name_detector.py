from typing import Dict, Optional

from detectors.detector import IDetector


class TeamNameDetector(IDetector):
    def __init__(self, prefix: str = "hacker"):
        self._prefix = prefix

    def detect(self, event_data: Dict) -> Optional[str]:
        team_name: str = event_data["name"]
        if team_name.startswith(self._prefix):
            return f"the team name {team_name} starts with the suspicious prefix {self._prefix}"
