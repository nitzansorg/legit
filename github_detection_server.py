from typing import Dict, List
from flask import Flask, request, make_response

from detectors.detector import IDetector
from notifiers.notifier import INotifier, Notification


class GithubDetectionServer(Flask):
    def __init__(self, notifier: INotifier, event_to_detector: Dict[str, List[IDetector]]):
        super().__init__(import_name=GithubDetectionServer.__name__)
        self.route('/', methods=['POST'])(self._handle_webhook)
        self._event_to_detector = event_to_detector
        self._notifier = notifier

    def _handle_webhook(self):
        event_type = request.headers["X-GitHub-Event"]
        event_data = request.json
        for detector in self._event_to_detector.get(event_type, []):
            suspect_reason = detector.detect(event_data)
            if suspect_reason:
                self._notifier.notify(Notification(event_type, suspect_reason))

        response = make_response('finished handling webhook', 200)
        return response
