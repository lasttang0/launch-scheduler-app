import datetime

from src.launch_date_finder import parse_raw_schedule, round_to_next_quarter, get_american_weekday, \
    find_next_launch_date


def test_parse_raw_schedule():
    """
    Test parsing a raw schedule string into a dictionary.

    Tests if the 'parse_raw_schedule' function correctly parses a raw schedule string and converts it into a dictionary.

    """
    raw_schedule = '''
        0,15;
        1,2;3,4;
        5,6;
        7,8;
    '''
    expected_schedule = {
        'quarters': [0, 15],
        'hours': [1, 2],
        'weekdays': [3, 4],
        'monthdays': [5, 6],
        'months': [7, 8]
    }
    assert parse_raw_schedule(raw_schedule) == expected_schedule


def test_round_to_next_quarter():
    """
    Test rounding a datetime to the next quarter.

    Tests if the 'round_to_next_quarter' function correctly rounds a given datetime to the next quarter-hour.

    """
    date = datetime.datetime(2023, 1, 1, 12, 7)
    expected_date = datetime.datetime(2023, 1, 1, 12, 15)
    assert round_to_next_quarter(date) == expected_date


def test_get_american_weekday():
    """
    Test getting the American-style weekday from a datetime.

    Tests if the 'get_american_weekday' function correctly retrieves the American-style weekday (1 to 7, where 1 is
    Sunday) from a given datetime.

    """
    date = datetime.datetime(2023, 1, 5)  # A Thursday
    expected_weekday = 5  # Thursday corresponds to 5 in the American-style weekday
    assert get_american_weekday(date) == expected_weekday


def test_find_next_launch_date():
    """
    Test finding the next launch date.

    Tests if the 'find_next_launch_date' function correctly finds the next launch date based on a provided schedule
    and starting date.

    """
    start_date = datetime.datetime(2023, 1, 1, 12, 0)
    sample_schedule = '0,15;12;1,2;1,2;1,2,3,4,5,6,7,8,9,10,11,12'
    expected_date = datetime.datetime(2023, 1, 1, 12, 0)  # Matches the start date
    assert find_next_launch_date(start_date, sample_schedule) == expected_date
