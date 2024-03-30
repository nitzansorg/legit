import logging

from github_detection_server import GithubDetectionServer
from detectors.repo_deletion_detector import RepoDeletionDetector
from detectors.team_name_detector import TeamNameDetector
from detectors.push_time_detector import PushTimeDetector
from notifiers.console_notifier import ConsoleNotifier

logging.basicConfig(filename='app.log', level=logging.INFO)

SIGNATURE = "this_is_signed"
EVENT_TO_DETECTOR = {"push": PushTimeDetector(),
                     "team": TeamNameDetector(),
                     "repository": RepoDeletionDetector()}

if __name__ == '__main__':
    app = GithubDetectionServer(SIGNATURE, ConsoleNotifier(), EVENT_TO_DETECTOR)
    app.run(debug=True)
