from datetime import datetime
from typing import Optional, Dict

from detectors.detector import IDetector
from github_time_utils import convert_github_time

BASIC_TIME_FORMAT = "%H:%M:%S"


class PushTimeDetector(IDetector):
    """
    detects a suspicious push by the time range it happened at
    """
    def __init__(self,
                 suspicious_start_time: str = "6:00:00",
                 suspicious_end_time: str = "23:00:00"):
        """
        :param suspicious_start_time: the start of the suspicious time range in UTC
        :param suspicious_end_time: the end of the suspicious time range in UTC
        """
        self._suspicious_start_time: datetime = datetime.strptime(suspicious_start_time, BASIC_TIME_FORMAT)
        self._suspicious_end_time: datetime = datetime.strptime(suspicious_end_time, BASIC_TIME_FORMAT)

    def detect(self, event_data: Dict) -> Optional[str]:
        push_time = convert_github_time(event_data["repository"]["pushed_at"])
        if self._suspicious_start_time.time() <= push_time.time() <= self._suspicious_end_time.time():
            return (f"the push time '{push_time}' was in the suspicious range "
                    f"'{self._suspicious_start_time}-{self._suspicious_end_time}'")



