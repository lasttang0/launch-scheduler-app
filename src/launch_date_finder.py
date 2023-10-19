from datetime import datetime, timedelta

QUARTER = 15
YEARS_TO_CHECK = 9999


def parse_raw_schedule(raw_schedule: str) -> dict:
    """
    Parse a raw schedule string and return a dictionary.

    Args:
        raw_schedule (str): A raw schedule string containing schedule intervals.

    Returns:
        dict: A dictionary with keys 'quarters', 'hours', 'weekdays', 'monthdays', and 'months'.

    """
    keys = ['quarters', 'hours', 'weekdays', 'monthdays', 'months']
    schedule_parts = raw_schedule.strip().replace('\n', '')[:-1].split(';')

    # We use a dict comprehension here to create the schedule dict.
    # We get keys and values for dict from zip object that forms from keys list and schedule parts.
    # Then we transform raw str value (such as '3,6,14,18,21,24,28') to int list, using both split(',') and map()
    # functions to create int numbers from str numbers.
    schedule = {key: list(map(int, value.split(','))) for key, value in zip(keys, schedule_parts)}
    return schedule


def round_to_next_quarter(date: datetime) -> datetime:
    """
    Rounds a datetime to the next multiple of 15 minutes.

    Args:
        date (datetime): The input datetime object.

    Returns:
        datetime: The rounded datetime object.

    """
    if date.minute % QUARTER == 0:
        return date
    minutes_to_next_quarter = QUARTER - date.minute % QUARTER
    delta = timedelta(minutes=minutes_to_next_quarter)
    return date + delta


def get_american_weekday(date: datetime) -> int:
    """
    Get the American-style weekday, where 1 is Sunday, 2 is Monday, and so on.

    Args:
        date (datetime): The input datetime object.

    Returns:
        int: The American-style weekday.

    """
    return date.isoweekday() % 7 + 1


def find_next_launch_date(start_date: datetime, raw_schedule: str):
    """
    Find the next launch date based on the provided schedule and starting date.

    Args:
        start_date (datetime): The starting date for the search.
        raw_schedule (str): A string representing the schedule to follow.

    Returns:
        datetime: The next launch date.

    Raises:
        ValueError: If the schedule is empty.

    """
    if not raw_schedule:
        raise ValueError('The schedule is empty')

    schedule = parse_raw_schedule(raw_schedule)
    next_quarter_date = round_to_next_quarter(start_date)

    while next_quarter_date.year <= start_date.year + YEARS_TO_CHECK:  # checks the next 9999 years
        if (next_quarter_date.minute in schedule['quarters'] and
                next_quarter_date.hour in schedule['hours'] and
                get_american_weekday(next_quarter_date) in schedule['weekdays'] and
                next_quarter_date.day in schedule['monthdays'] and
                next_quarter_date.month in schedule['months']):
            return next_quarter_date  # success
        else:
            next_quarter_date += timedelta(minutes=QUARTER)  # step = 15min

    return None  # no suitable date found over 9999 years
