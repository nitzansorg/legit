import abc
from typing import Optional, Dict


class IDetector(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def detect(self, event_data: Dict) -> Optional[str]:
        """
        Detects weather the given event_data indicates on suspicious behaviour
        :return: the appropriate alert if there is any
        """
        raise NotImplementedError
