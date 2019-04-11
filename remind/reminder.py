from datetime import datetime

from util import time_date


class Reminder:
    def __init__(self, time_str: str, title: str, note: str, _datetime: datetime = None):
        self.title = title
        self.note = note
        self.time_str = time_str

        if _datetime:
            self.time = _datetime
        else:
            self.time = time_date.datetime_from_str(self.time_str)


