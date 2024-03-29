from github_detection_server import GithubDetectionServer
from detectors.repo_deletion_detector import RepoDeletionDetector
from detectors.team_name_detector import TeamNameDetector
from detectors.push_time_detector import PushTimeDetector

EVENT_TO_DETECTORS = {"push": [PushTimeDetector()], "team": [TeamNameDetector()],
                      "repository": [RepoDeletionDetector()]}

if __name__ == '__main__':
    app = GithubDetectionServer(EVENT_TO_DETECTORS)
    app.run(debug=True)
