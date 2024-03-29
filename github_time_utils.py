from datetime import datetime, timedelta

GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
BASIC_TIME_FORMAT = "%H:%M:%S"


def is_time_in_range(to_check: str, start_time: str, end_time: str) -> bool:
    """
    checks if the given gitHub time is between the two given times
    :param to_check: a str representing a time in the gitHub format
    :param start_time: a str representing a time in the normal format
    :param end_time: a str representing a time in the normal format
    :return: true if the time is in the given range
    """
    to_check = datetime.strptime(to_check, GITHUB_TIME_FORMAT).time()

    start_time = datetime.strptime(start_time, BASIC_TIME_FORMAT).time()
    end_time = datetime.strptime(end_time, BASIC_TIME_FORMAT).time()

    return start_time <= to_check <= end_time


def are_times_close(start_time: str, end_time: str, close_delta: timedelta) -> bool:
    """
    checks if the two given times are close, meaning the difference between them is less then the given timedelta
    :param start_time: a str representing a time in the gitHub format
    :param end_time: a str representing a time in the gitHub format
    :param close_delta: the timedelta that is considered close
    :return: true if the two times are close to each-other
    """
    start_time = datetime.strptime(start_time, GITHUB_TIME_FORMAT)
    end_time = datetime.strptime(end_time, GITHUB_TIME_FORMAT)
    return (end_time - start_time) < close_delta
