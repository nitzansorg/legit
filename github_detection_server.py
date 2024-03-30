from typing import Dict
from flask import Flask, request, make_response, Response

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
        response = self._verify_request()
        if response:
            return response

        self._detect()

        return make_response('finished handling webhook', 200)

    def _verify_request(self) -> Response:
        """
        :return: the appropriate response if the request wasn't verified
        """
        signature = request.headers.get("x-hub-signature-256")
        if not is_signature_verified(request.data, self._token, signature):
            self.logger.warning(f"received an unverified request.\n"
                                f"request: {request}")
            return make_response('unauthorized to make requests', 403)

    def _detect(self):
        event_type = request.headers.get("X-GitHub-Event")
        detector = self._event_to_detector.get(event_type)

        if detector:

            try:
                suspect_reason = detector.detect(request.json)
            except ValueError as e:
                self.logger.warning(f"found missing parameters - the request didn't go through detection.\n"
                                    f"request: {request}\n"
                                    f"detector: {detector}\n"
                                    f"error: {e}")
                return make_response("couldn't handle the request do to missing parameters", 400)

            if suspect_reason:
                self.logger.info(f"detected a suspicious behaviour.\n"
                                 f"detector: {detector}\n"
                                 f"request: {request}")
                self._notifier.notify(Notification(event_type, suspect_reason))
