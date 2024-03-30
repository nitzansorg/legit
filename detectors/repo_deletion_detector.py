from datetime import timedelta
from typing import Dict, Optional

from detectors.detector import IDetector
from github_time_utils import convert_github_time


class RepoDeletionDetector(IDetector):
    """
    Detects a suspicious repo deletion by the time between the repo creation and it's deletion
    """
    def __init__(self, close_delta: timedelta = timedelta(minutes=10)):
        self._close_delta = close_delta

    def detect(self, event_data: Dict) -> Optional[str]:
        if event_data["action"] != "deleted":
            return  # this detector detects suspicious deletion only
        creation_time = convert_github_time(event_data["repository"]["created_at"])
        deletion_time = convert_github_time(event_data["repository"]["updated_at"])
        if (deletion_time - creation_time) < self._close_delta:
            repo_name = event_data["repository"]["name"]
            return (f"the deletion of repository '{repo_name}' happened in the suspicious time delta "
                    f"'{self._close_delta}' after the creation of the repo")

