from typing import Optional, Dict

from detectors.detector import IDetector
from github_time_utils import is_time_in_range


class UpdateTimeDetector(IDetector):
    """
    detects a suspicious repo update by the time range it happened at
    """
    def __init__(self,
                 suspicious_start_time: str = "10:00:00",
                 suspicious_end_time: str = "20:00:00"):
        self._suspicious_start_time = suspicious_start_time
        self._suspicious_end_time = suspicious_end_time

    def detect(self, event_data: Dict) -> Optional[str]:
        push_time = event_data["repository"]["updated_at"]
        if is_time_in_range(push_time, self._suspicious_start_time, self._suspicious_end_time):
            return f"the update time '{push_time}' was in the suspicious range '{self._suspicious_start_time}-{self._suspicious_end_time}'"



