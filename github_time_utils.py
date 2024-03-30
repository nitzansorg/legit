from datetime import datetime


def convert_github_time(time) -> datetime:
    if isinstance(time, str):
        return datetime.fromisoformat(time)
    else:  # assume the time is a timestamp
        return datetime.utcfromtimestamp(time)
