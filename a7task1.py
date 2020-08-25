#
# a7task1.py - Assignment 7, Task 1
# Name: Minheng Xiao
# Email address: minhengx@bu.edu
# Description: A Date class
#

class Date:

    # Puzzle1:
    def __init__(self, new_month, new_day, new_year):
        """
        :param new_month: Assign month to class object month
        :param new_day: Assign day to class object day
        :param new_year: Assign year to class object year
        """
        self.month, self.day, self.year = new_month, new_day, new_year

    def __repr__(self):
        """
        :return: return in format 'mm/dd/yyyy'
        """
        return "%02d/%02d/%4d" % (self.month, self.day, self.year)

    def copy(self):
        """
        :return: Return a newly-constructed object of type
                 Date with the same month, day, and year
        """
        return Date(self.month, self.day, self.year)


    # Puzzle2:
    def is_leap_year(self):
        """
        :return: if the object is a leap year
        """
        return bool((not self.year % 400) or (not self.year % 4 and self.year % 100))

    # Puzzle3:
    def is_valid_date(self):
        """

        :return:
        """
        if self.month == 2:
            return bool((self.month in list(range(1, 13))) and\
                        (self.day in list(range(1, 30) if self.is_leap_year() else range(1, 29))))
        else:
            return bool((self.month in list(range(1, 13))) and\
                        (self.day in list(range(1, 31) if self.month in [4, 6, 9, 11] else range(1, 32))))

    # Puzzle4:
    def add_one_day(self):
        """

        :return:
        """
        assert self.is_valid_date(), "Not a valid date"
        self.day += 1
        if not self.is_valid_date():
            self.day = 1
            self.month += 1
            if not self.is_valid_date():
                self.month = 1
                self.year += 1
        return None

    # Puzzle5:
    def rem_one_day(self):
        """

        :return:
        """
        assert self.is_valid_date(), "Not a valid day"

        self.day -= 1
        if not self.is_valid_date():
            if self.month != 1:
                self.month -= 1
                self.day = 31
                while not self.is_valid_date():
                    self.day -= 1
            else:
                self.year -= 1
                self.month = 12
                self.day = 31

    # Puzzle6:
    def add_n_days(self, n):
        """

        :param n:
        :return:
        """
        print(self)
        for _ in range(n):
            self.add_one_day()
            print(self)

    # Puzzle7:
    def rem_n_days(self, n):
        """

        :param n:
        :return:
        """
        print(self)
        for _ in range(n):
            self.rem_one_day()
            print(self)

    # Puzzle8
    def __eq__(self, other):
        """
        :param other: Other Date object
        :return: return if these two objects are the same
        """
        return bool(self.day == other.day and self.month == other.month and self.year == other.year)

    # Puzzle9:
    def is_before(self, other):
        """

        :param other:
        :return:
        """
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        else:
            return False

    # Puzzle10:
    def is_after(self, other):
        """

        :param other:
        :return:
        """
        return not self.is_before(other) and not self == other

    # Puzzle11:
    def diff(self, other):
        """

        :param other:
        :return:
        """
        other_copy = other.copy()
        n = 0
        while not self == other_copy:
            if self.is_before(other_copy):
                n -= 1
                other_copy.rem_one_day()
            else:
                n += 1
                other_copy.add_one_day()
        return n

    # Puzzle12:
    def day_of_week(self):
        """

        :return:
        """
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        critical_date = Date(8, 24, 2020)
        n = self.diff(critical_date)
        return day_of_week_names[n % 7]







