from datetime import datetime, timedelta

GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
BASIC_TIME_FORMAT = "%H:%M:%S"


def is_time_in_range(to_check: str, start_time: str, end_time: str) -> bool:
    to_check = datetime.strptime(to_check, GITHUB_TIME_FORMAT).time()

    start_time = datetime.strptime(start_time, BASIC_TIME_FORMAT).time()
    end_time = datetime.strptime(end_time, BASIC_TIME_FORMAT).time()

    return start_time <= to_check <= end_time


def are_times_close(start_time: str, end_time: str, close_delta: timedelta) -> bool:
    start_time = datetime.strptime(start_time, GITHUB_TIME_FORMAT)
    end_time = datetime.strptime(end_time, GITHUB_TIME_FORMAT)
    return (end_time - start_time) < close_delta
