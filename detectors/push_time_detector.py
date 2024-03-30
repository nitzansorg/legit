from datetime import datetime
from typing import Optional, Dict

from detectors.detector import IDetector
from github_time_utils import is_time_in_range, convert_github_timestamp


class PushTimeDetector(IDetector):
    """
    detects a suspicious repo update by the time range it happened at
    """
    def __init__(self,
                 suspicious_start_time: str = "10:00:00",
                 suspicious_end_time: str = "23:00:00"):
        self._suspicious_start_time: str = suspicious_start_time
        self._suspicious_end_time: str = suspicious_end_time

    def detect(self, event_data: Dict) -> Optional[str]:
        push_time = convert_github_timestamp(event_data["repository"]["pushed_at"])
        if is_time_in_range(push_time, self._suspicious_start_time, self._suspicious_end_time):
            return (f"the update time '{push_time}' was in the suspicious range "
                    f"'{self._suspicious_start_time}-{self._suspicious_end_time}'")



