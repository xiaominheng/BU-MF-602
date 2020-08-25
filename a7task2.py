#
# a7task2.py - Assignment 7, Task 2
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: Some Date clients
#
from a7task1 import *

# Puzzle1:
def options_expiration_days(year):
    """

    :param year:
    :return:
    """
    fridays = [[Date(month, day, year) for day in range(1, 32)\
                if Date(month, day, year).is_valid_date()\
                and Date(month, day, year).day_of_week() == "Friday"]\
               for month in range(1, 13)]
    third_fridays = [fridays[i][2] for i in range(12)]
    return third_fridays

# Puzzle2:
def market_holidays(year):
    """

    :param year:
    :return:
    """
    # New year is the January 1st if not Sunday, or January 2nd.
    new_year = Date(1, 1, year) if Date(1, 1, year).day_of_week() != "Sunday" else Date(1, 2, year)

    # Martin Luther King's Day is the third Monday in January
    mlk = [Date(1, i, year) for i in range(1, 32) if Date(1, i, year).day_of_week() == "Monday"][2]

    # President’s Day (the third Monday in February)
    president_day = [Date(2, i, year) for i in range(1, 30) if Date(2, i, year).is_valid_date() and\
                     Date(2, i, year).day_of_week() == "Monday"][2]

    # Memorial Day (the last Monday in May)
    memorial_day = [Date(5, i, year) for i in range(1, 32) if Date(5, i, year).day_of_week() == "Monday"][-1]

    # Independence Day (July 4th, observed on July 5th if July 4th is a Sunday)
    independence_day = Date(7, 4, year) if Date(7, 4, year).day_of_week() != "Sunday" else Date(7, 5, year)

    # Labor Day (the first Monday in September)
    labor_day = [Date(9, i, year) for i in range(1, 31) if Date(9, i, year).day_of_week() == "Monday"][0]

    # Thanksgiving Day (the fourth Thursday in November)
    thanksgiving_day = [Date(11, i, year) for i in range(1, 31) if Date(11, i, year).day_of_week() == "Thursday"][3]

    # Christmas Day (the 25th of December, observed on December 26th if the 25th is a Sunday)
    christmas_day = Date(12, 25, year) if Date(12, 25, year).day_of_week() != "Sunday" else Date(12, 26, year)

    print("New Year's Day is observed on %s %s" % (new_year.day_of_week(), new_year))
    print("Martin Luther King Day is observed on Monday %s" % mlk)
    print("President's Day is observed on Monday %s" % president_day)
    print("Memorial Day is observed on Monday %s" % memorial_day)
    print("Independence Day is observed on %s %s" % (independence_day.day_of_week(), independence_day))
    print("Labor Day is observed on %s" % labor_day)
    print("Thanksgiving Day is observed on Thursday %s" % thanksgiving_day)
    print("Christmas Day is observed on %s %s" % (christmas_day.day_of_week(), christmas_day))

    return [new_year, mlk, president_day, memorial_day, independence_day, labor_day, thanksgiving_day, christmas_day]

