from datetime import datetime

GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
BASIC_TIME_FORMAT = "%H:%M:%S"


def is_time_in_range(to_check: str, start_time: str, end_time: str) -> bool:
    to_check = datetime.strptime(to_check, GITHUB_TIME_FORMAT)

    start_time = datetime.strptime(start_time, BASIC_TIME_FORMAT).time()
    end_time = datetime.strptime(end_time, BASIC_TIME_FORMAT).time()

    return start_time <= to_check.time() <= end_time
