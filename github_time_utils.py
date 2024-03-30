from datetime import datetime, timedelta

GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
BASIC_TIME_FORMAT = "%H:%M:%S"


def convert_github_time(time) -> datetime:
    if isinstance(time, str):
        return datetime.fromisoformat(time)
    else:  # assume the time is a timestamp
        return datetime.utcfromtimestamp(time)


def is_time_in_range(to_check: datetime, start_time: str, end_time: str) -> bool:
    """
    check weather the given time is between the start and end time
    """
    start_time = datetime.strptime(start_time, BASIC_TIME_FORMAT).time()
    end_time = datetime.strptime(end_time, BASIC_TIME_FORMAT).time()
    return start_time <= to_check.time() <= end_time


def are_times_close(start_time: datetime, end_time: datetime, close_delta: timedelta) -> bool:
    """
    checks if the two given times are close, meaning the difference between them is less then the given timedelta
    :param start_time: a str representing a time in the gitHub format
    :param end_time: a str representing a time in the gitHub format
    :param close_delta: the timedelta that is considered close
    :return: true if the two times are close to each-other
    """
    return (end_time - start_time) < close_delta
