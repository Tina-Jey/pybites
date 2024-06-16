import calendar
from datetime import date


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    x = date

    return days[x.weekday()]
