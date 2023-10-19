import pytest
from datetime import datetime
from src.launch_date_finder import find_next_launch_date


# Testing when the schedule is empty
def test_empty_schedule():
    with pytest.raises(ValueError):
        find_next_launch_date(datetime(2023, 1, 1, 12, 0), '')


# Testing when date and time in the schedule are reachable
def test_valid_schedule():
    sample_date = datetime(2023, 1, 1, 12, 0)
    sample_schedule = '0,15,30,45;12,18;1,2,3,4,5,6,7;1,2,3,4;1,2,3,4,5,6,7,8,9,10,11,12'
    result = find_next_launch_date(sample_date, sample_schedule)
    assert result == datetime(2023, 1, 1, 12, 0)


# Testing when date and time in the schedule are not reachable
def test_no_valid_schedule():
    sample_date = datetime(2023, 1, 1, 12, 0)
    sample_schedule = '99,100,101;20,21;8,9;5,6;7,8,9,10,11,12'
    result = find_next_launch_date(sample_date, sample_schedule)
    assert result is None
