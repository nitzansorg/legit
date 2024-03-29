from flask import Flask, request

from detectors.push_detector import TimeDetector

app = Flask(__name__)

EVENT_TO_DETECTORS = {"push": [TimeDetector()]}


@app.route('/', methods=["post"])
def handle_webhook():
    event_type = request.headers["X-GitHub-Event"]
    event_data = request.json
    print(event_data)
    for detector in EVENT_TO_DETECTORS[event_type]:
        alert = detector.detect(event_data)
        if alert:
            print(f"event of type {event_type} was detected as suspicious, because {alert}")


if __name__ == '__main__':
    app.run(debug=True)
