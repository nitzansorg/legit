from datetime import timedelta
from typing import Dict, Optional

from detectors.detector import IDetector
from github_time_utils import convert_github_time


class RepoDeletionDetector(IDetector):
    """
    Detects a suspicious repo deletion by the time between the repo creation and it's deletion
    """
    def __init__(self, close_delta: timedelta = timedelta(seconds=5)):
        self._close_delta = close_delta

    def detect(self, event_data: Dict) -> Optional[str]:
        if event_data.get("action") != "deleted":
            return  # this detector detects suspicious deletion only
        repo_data = event_data.get("repository")
        if not repo_data:
            raise ValueError("missing repo data")
        creation_time = repo_data.get("created_at")
        deletion_time = repo_data.get("updated_at")
        if not creation_time or not deletion_time:
            raise ValueError("missing creation or deletion time")
        creation_time = convert_github_time(creation_time)
        deletion_time = convert_github_time(deletion_time)
        if (deletion_time - creation_time) <= self._close_delta:
            repo_name = repo_data.get("name")
            return (f"the deletion of repository '{repo_name}' happened in the suspicious time delta "
                    f"'{self._close_delta}' after the creation of the repo")

