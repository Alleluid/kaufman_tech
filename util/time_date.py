from datetime import datetime, timedelta


def timedelta_from_str(delta_str: str, default: timedelta = timedelta(days=1), strip_secs=True) -> timedelta:
    """Matches a string of [num unit(s)] to the described `timedelta`.

    :param delta_str:
    :param default: `timedelta` used if string doesn't match. Default is 1 day.
    :return:
    """

    split_str = delta_str.split(' ')
    # If it gets here but has no space, it must be an iso attempt
    if len(split_str) == 1:
        raise ValueError("Incorrect formatting, not iso format nor [num] [unit]")

    # Split string, assign each element to vars, ensure `num` is a number before casting it.
    num, unit, *other = split_str
    if not num.isnumeric():
        raise TypeError("First element in string must be int")
    num = int(num)

    got = {
        ("year", "years"): timedelta(days=num * 365),
        ("month", "months"): timedelta(days=num * 30),
        ("week", "weeks"): timedelta(weeks=num),
        ("day", "days"): timedelta(days=num),
        ("hour", "hours"): timedelta(hours=num),
        ("minute", "minutes", "min", "mins"): timedelta(minutes=num)
    }

    # Oh boy, recursion!
    additional_time = timedelta()
    if other:
        additional_time = timedelta_from_str(' '.join(other), default)

    for tup, td in got.items():
        if unit in tup:
            final_delta = td + additional_time
            break
    else:
        final_delta = default + additional_time

    return strip_seconds(final_delta) if strip_secs else final_delta


def datetime_from_str(time_str: str, default: timedelta = timedelta(days=1), strip_secs=True) -> datetime:
    """Matches an iso formatted, or a natural language datetime string.

    Matches iso format YYYY-MM-DDTHH:MM:SS
    The `T` is literal, it and any unit after it is optional.
    :param time_str:
    :param default: `timedelta` used if string doesn't match. Default is 1 day.
    :param strip_secs: Removes seconds and smaller from time.
    :return:
    """
    # TODO: add preferences support, ex. anything more than 1 day from now happens at a set time.
    try:
        final_datetime = datetime.fromisoformat(time_str)
    except ValueError:
        delta = timedelta_from_str(time_str, default, strip_secs)
        final_datetime = datetime.now() + delta
    return strip_seconds(final_datetime) if strip_secs else final_datetime


def now_plus(**kwargs) -> datetime:
    if "months" in kwargs.keys():
        # TODO: Go down the rabbit hole of making this more accurate
        return datetime.now() + timedelta(days=kwargs["months"] * 30)
    elif "years" in kwargs.keys():
        return datetime.now() + timedelta(days=kwargs["years"] * 365)
    else:
        return datetime.now() + timedelta(**kwargs)

def strip_seconds(time_type):
    # Gets time in seconds, rounds to remove millis if needed, removes modulo 60 to strip seconds
    if isinstance(time_type, timedelta):
        return timedelta(seconds=time_type.total_seconds() - time_type.total_seconds() % 60)
    elif isinstance(time_type, datetime):
        # If it's before unix epoch, oh well
        if time_type.timestamp() < 1:
            return time_type
        return datetime.fromtimestamp(round(time_type.timestamp() - time_type.timestamp() % 60))
    else:
        return None


if __name__ == '__main__':
    print(datetime.now())
    print(datetime_from_str("3 hours"))
    print(datetime_from_str("50 mins"))
    print(datetime_from_str("36 days"))
    print(datetime_from_str("1 year"))
    print(datetime_from_str("2019-05-15"))
    print(datetime_from_str("1800-01-01T12:00"))
    print(datetime_from_str("9999-12-31T23:59"))
