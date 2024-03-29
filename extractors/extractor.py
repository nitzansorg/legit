import abc
from typing import Optional, Dict, Any


class IExtractor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def extract(self, event_data: Dict) -> Any:
        """
        extracts specific information from the event data
        """
        raise NotImplementedError
