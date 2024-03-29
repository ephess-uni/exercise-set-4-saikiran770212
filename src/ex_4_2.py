""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    Convert  a string representing a date and time into datetime object
    """
    return datetime.strptime(datestr, "%Y-%m-%dT%H:%M:%S")


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
