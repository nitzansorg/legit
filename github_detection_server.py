from typing import Dict, List
from flask import Flask, request, make_response

from detectors.detector import IDetector
from notifiers.notifier import INotifier, Notification
from webhook_validator import is_signature_verified


class GithubDetectionServer(Flask):
    """
    A basic http-server that receives gitHub webhooks and runs detectors for suspicious behaviour on their content
    """
    def __init__(self, token: str, notifier: INotifier, event_to_detector: Dict[str, IDetector]):
        super().__init__(import_name=GithubDetectionServer.__name__)
        self._token = token
        self._event_to_detector = event_to_detector
        self._notifier = notifier
        self.route('/', methods=['POST'])(self._handle_webhook)

    def _handle_webhook(self):
        signature = request.headers.get("x-hub-signature-256")
        if not is_signature_verified(request.data, self._token, signature):
            return make_response('unauthorized to make requests', 403)

        event_type = request.headers.get("X-GitHub-Event")
        event_data = request.json
        detector = self._event_to_detector.get(event_type)
        if detector:
            suspect_reason = detector.detect(event_data)
            if suspect_reason:
                self._notifier.notify(Notification(event_type, suspect_reason))

        return make_response('finished handling webhook', 200)
