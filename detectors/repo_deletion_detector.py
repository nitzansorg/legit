from datetime import timedelta
from typing import Dict, Optional

from detectors.detector import IDetector
from github_time_utils import are_times_close


class RepoDeletionDetector(IDetector):
    def __init__(self, close_delta: timedelta = timedelta(minutes=10)):
        self._close_delta = close_delta

    def detect(self, event_data: Dict) -> Optional[str]:
        if event_data["action"] != "deleted":
            return  # we are only interested in a deletion at this detector
        creation_time = event_data["repository"]["created_at"]
        deletion_time = event_data["repository"]["updated_at"]
        if are_times_close(creation_time, deletion_time, self._close_delta):
            repo_name = event_data["repository"]["name"]
            return (f"the deletion of repository '{repo_name}' happened in the suspicious time delta "
                    f"'{self._close_delta}' after the creation of the repo")

