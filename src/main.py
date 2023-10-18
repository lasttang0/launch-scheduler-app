import configparser
from datetime import datetime

from src.launch_date_finder import find_next_launch_date


def main():
    """
    Main function to read a configuration file, parse a date, and find the next launch date.

    Reads a configuration file ('config.cfg') containing 'sample_date' and 'sample_schedule' settings,
    parses the 'sample_date' as a datetime object, and uses it with 'sample_schedule' to find the next launch date.

    Returns:
        None

    """
    config = configparser.ConfigParser()
    config.read('config.cfg')

    sample_date = config['data']['sample_date']
    sample_schedule = config['data']['sample_schedule']

    print(find_next_launch_date(datetime.strptime(sample_date, '%d.%m.%Y %H:%M'), sample_schedule))


if __name__ == '__main__':
    main()
