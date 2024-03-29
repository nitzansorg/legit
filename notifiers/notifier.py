import abc
from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class Notification:
    event_type: str
    suspect_reason: str


class INotifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def notify(self, notification: Notification):
        """
        notify the user about the given notification
        """
        raise NotImplementedError
