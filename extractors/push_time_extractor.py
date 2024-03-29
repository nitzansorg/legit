from typing import Dict, Any

from extractors.extractor import IExtractor


class PushTimeExtractor(IExtractor):
    def extract(self, event_data: Dict) -> Any:
        pass
