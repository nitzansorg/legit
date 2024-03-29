from datetime import datetime
from typing import Optional, Dict

from detectors.detector import IDetector

GITHUB_TIME_FORMAT = ""
BASIC_TIME_FORMAT = ""


class TimeDetector(IDetector):
    def __init__(self, suspicious_start_time="14:00:00", suspicious_end_time="16:00:00"):
        self._suspicious_start_time = suspicious_start_time
        self._suspicious_end_time = suspicious_end_time

    def detect(self, event_data: Dict) -> Optional[str]:
        time = event_data["updated_at"]
        if _is_time_in_range(time, self._suspicious_start_time, self._suspicious_end_time):
            return f"suspicious time: {time} was in range {self._suspicious_start_time}-{self._suspicious_end_time}"


def _is_time_in_range(to_check: str, start_time, end_time) -> bool:
    to_check = datetime.strptime(to_check, GITHUB_TIME_FORMAT)

    start_time = datetime.strptime(start_time, BASIC_TIME_FORMAT).time()
    end_time = datetime.strptime(end_time, BASIC_TIME_FORMAT).time()

    return start_time <= to_check.time() <= end_time