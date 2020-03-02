import math
from datetime import datetime

def firstrun():
    return "success"


def circle_area(radius):
    return math.pi * pow(radius, 2)


def first_and_last(contents):

    if contents == []:
        return None
    return contents[0], contents[-1]


def days_between_days(strdate1, strdate2):

    date_format = "%m/%d/%Y"
    date1 = datetime.strptime(strdate1, date_format)
    date2 = datetime.strptime(strdate2, date_format)
    delta = date2 - date1
    return delta.days
