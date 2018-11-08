import datetime


def find_closest_next_from_now(microsecond: int, second: int = None, minute: int = None, hour: int = None):
    first = datetime.datetime.now()

    first = first.replace(microsecond=microsecond)
    duration = datetime.timedelta(seconds=1)

    if second is not None:
        first = first.replace(second=second)
        duration = datetime.timedelta(minutes=1)

    if minute is not None:
        first = first.replace(minute=minute)
        duration = datetime.timedelta(hours=1)

    if hour is not None:
        first = first.replace(hour=hour)
        duration = datetime.timedelta(days=1)

    now = datetime.datetime.now()

    if now > first:
        while now > first:
            first += duration
    else:
        while now < first:
            first -= duration
        first += duration

    return first


def current_time_string_second(t=None):
    return datetime.datetime.now().strftime('%H:%M:%S') if t is None else t.strftime('%H:%M:%S')


def current_time_string_fraction(t=None):
    return datetime.datetime.now().strftime('%H:%M:%S.%f')[:-4] if t is None else t.strftime('%H:%M:%S.%f')[:-4]


def ctss(t=None):
    return current_time_string_second(t)


def ctsf(t=None):
    return current_time_string_fraction(t)

