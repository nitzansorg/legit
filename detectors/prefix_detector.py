from typing import Dict, Optional

from detectors.detector import IDetector


class PrefixDetector(IDetector):
    def __init__(self, prefix: str):
        self._prefix = prefix

    def detect(self, event_data: Dict) -> Optional[str]:
        to_check: str = event_data
        if to_check.startswith(self._prefix):
            return f"the parameter {to_check} starts with the suspicious prefix {self._prefix}"
