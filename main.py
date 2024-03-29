from github_detection_server import GithubDetectionServer
from detectors.repo_deletion_detector import RepoDeletionDetector
from detectors.team_name_detector import TeamNameDetector
from detectors.update_time_detector import UpdateTimeDetector
from notifiers.console_notifier import ConsoleNotifier

EVENT_TO_DETECTORS = {"push": [UpdateTimeDetector()],  # push is update
                      "team": [TeamNameDetector()],
                      "repository": [RepoDeletionDetector()]}

if __name__ == '__main__':
    app = GithubDetectionServer(ConsoleNotifier(), EVENT_TO_DETECTORS)
    app.run(debug=True)
