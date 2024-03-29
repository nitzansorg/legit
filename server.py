from flask import Flask, request, make_response

from detectors.time_range_detector import TimeRangeDetector

app = Flask(__name__)

EVENT_TO_DETECTORS = {"push": [TimeRangeDetector()]}


@app.route('/', methods=["post"])
def handle_webhook():
    event_type = request.headers["X-GitHub-Event"]
    event_data = request.json
    for detector in EVENT_TO_DETECTORS[event_type]:
        alert = detector.detect(event_data)
        if alert:
            print(f"event of type {event_type} was detected as suspicious, because {alert}")

    response = make_response('finished handling webhook', 200)
    return response


if __name__ == '__main__':
    app.run(debug=True)
