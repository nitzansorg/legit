from typing import Dict, List
from flask import Flask, request, make_response

from detectors.detector import IDetector


class GithubDetectionServer(Flask):
    def __init__(self, event_to_detector: Dict[str, List[IDetector]]):
        super().__init__(import_name=GithubDetectionServer.__name__)
        self.route('/', methods=['POST'])(self._handle_webhook)
        self._event_to_detector = event_to_detector

    def _handle_webhook(self):
        event_type = request.headers["X-GitHub-Event"]
        event_data = request.json
        for detector in self._event_to_detector.get(event_type, []):
            alert = detector.detect(event_data)
            if alert:
                print(f"event of type {event_type} was detected as suspicious, because {alert}")

        response = make_response('finished handling webhook', 200)
        return response
