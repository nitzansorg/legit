import abc
from typing import Optional, Dict


class INotifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self, alert: str):
        """
        notify the user about the given alert
        """
        raise NotImplementedError
