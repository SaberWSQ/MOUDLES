"""
Program: half_birthday.py
Author: Shiqi Wang
Last date modified: 10/13/2020


The purpose of this program is to write a function to return the six month later date
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta


def half_birthday(time):
    """Return six month later of the time

    :param datetime time: input birthday
    :return: datetime
    """
    return time + relativedelta(months=+6)


def main():
    time = datetime.now()
    print(f"Today: {time}")
    print(f"Six months later: {half_birthday(time)}")


if __name__ == '__main__':
    main()
