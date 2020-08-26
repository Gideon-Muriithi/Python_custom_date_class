# a7task1.py - Assignment 7, Task 1
#
# A Date Class to represent objects that are calender dates
#

import copy


class Date:
    """Date class for creating date objects which represent calender dates."""

    def __init__(self, new_month, new_day, new_year):
        """A constructor for Date objects."""

        self.new_month = new_month
        self.new_day = new_day
        self.new_year = new_year

    def __repr__(self):
        return (
            ("0" + str(self.new_month) if self.new_month < 10 else str(self.new_month))
            + "/"
            + ("0" + str(self.new_day) if self.new_day < 10 else str(self.new_day))
            + "/"
            + str(self.new_year)
        )

    def copy(self):
        """Returns a newly-constructed object of type Date with the same month, day, 
        and year that the called object has.
        """

        return Date

    def is_leap_year(self):
        """Returns True if the called object is in a leap year, and False otherwise."""

        if (
            self.new_year % 4 == 0 and self.new_year % 100 != 0
        ):  # Check if new_year is divisible by 4 and not divisible by 100
            return True

        elif self.new_year % 400 == 0:  # Check if new_year is divisible by 400
            return True

        else:
            return False

    def is_valid_date(self):
        """Returns True if the object is a valid date, and False otherwise."""

        if (
            self.new_month > 0 and self.new_month <= 12
        ):  # Check if month falls between numbers 1 to 12

            if (
                self.new_month == 1
                or self.new_month == 3
                or self.new_month == 5
                or self.new_month == 7
                or self.new_month == 8
                or self.new_month == 10
                or self.new_month == 12
            ):  # Check if month falls between January, March, May, July, August, October or December.
                if self.new_day > 0 and self.new_day <= 31:
                    # Return True if day passed is between 0 and 31.
                    return True

                else:
                    # Return False if day passed is not between 0 and 31.
                    return False

            elif (
                self.new_month == 4
                or self.new_month == 6
                or self.new_month == 9
                or self.new_month == 11
            ):  # Check if month falls between April, June, September, or November.
                if self.new_day > 0 and self.new_day <= 30:
                    # Return True if day passed is between 0 and 30.
                    return True

                else:
                    # Return False if day passed is not between 0 and 30.
                    return False

            elif self.new_month == 2:  # Check if month falls in February.
                if self.is_leap_year() == True:  # Check if year is a leap year.
                    if self.new_day > 0 and self.new_day <= 29:
                        # Return True if day passed is between 0 and 29
                        return True

                    else:
                        # Return False if day passed is not between 0 and 29.
                        return False

                elif self.is_leap_year() == False:  # Check if year is not a leap year.
                    if self.new_day > 0 and self.new_day <= 28:
                        # Return True if day passed is between 0 and 28
                        return True

                    else:
                        # Return False if day passed is not between 0 and 28
                        return False

        else:
            # Return False if month does not fall between numbers 1 to 12
            return False

    def add_one_day(self):
        """Changes the called object so that it represents one calendar 
        day after the date that it originally represented.
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_month_in_date_object = days_in_month[self.new_month]

        if (
            days_month_in_date_object == 31 and self.is_valid_date() == True
        ):  # Check if day is end month
            if (
                self.new_month != 12 and self.new_day == 31
            ):  # Check that month not December.
                # Change day and month if end month and month not December.
                self.new_day = 1
                self.new_month = self.new_month + 1
            elif self.new_month == 12 and self.new_day == 31:
                # Change day, month and year if end month and month is December.
                self.new_day = 1
                self.new_month = 1
                self.new_year = self.new_year + 1

            else:
                # Change day if not end month.
                self.new_day = self.new_day + 1

        elif (
            days_month_in_date_object == 30 and self.is_valid_date() == True
        ):  # Check if day is end month
            if (
                self.new_month != 12 and self.new_day == 30
            ):  # Check that month not December.
                # Change day and month if end month and month not December.
                self.new_day = 1
                self.new_month = self.new_month + 1

            elif self.new_month == 12:
                # Change day, month and year if end month and month is December.
                self.new_day = self.new_day + 1

            else:
                # Change day if not end month.
                self.new_day = self.new_day + 1

        elif (
            days_month_in_date_object == 28
            and self.is_leap_year() != True
            and self.new_month == 2
            and self.is_valid_date() == True
        ):  # Check if day is end month and year not a leap year
            if self.new_day == 28:
                self.new_day = 1
                self.new_month = self.new_month + 1

            else:
                # Change day if end month and year is leap year and not end month.
                self.new_day = self.new_day + 1

        elif (
            self.is_leap_year() == True
            and self.new_month == 2
            and self.is_valid_date() == True
        ):  # Check if year is a leap year.

            if self.new_day == 29:
                # Change day, month if end month and year is leap year.
                self.new_day = 1
                self.new_month = self.new_month + 1

            else:
                # Change day if end month and year is leap year and not end month.
                self.new_day = self.new_day + 1

    def rem_one_day(self):
        """Changes the called object so that it represents one calendar 
            day before the date that it originally represented.
            """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_month_in_date_object = days_in_month[self.new_month]

        if (
            days_month_in_date_object == 31
            or days_month_in_date_object == 30
            and self.is_valid_date() == True
            and self.new_month != 3
        ):
            if (
                self.new_day != 1 and self.new_month != 1
            ):  # Check that month not January.
                # Change day beginning of month and not beginning of year.
                self.new_day = self.new_day - 1

            elif self.new_month == 1 and self.new_day == 1:
                # Change day, month and year if beginning of month and month is January.
                self.new_month = 12
                self.new_day = days_in_month[self.new_month]
                self.new_year = self.new_year - 1

            elif self.new_day == 1:
                # Change day, month if beginning of month and month is not January.
                self.new_month = self.new_month - 1
                self.new_day = days_in_month[self.new_month]

        elif (
            days_month_in_date_object == 31
            and self.new_month == 3
            and self.is_valid_date() == True
        ):  # Check if month is March

            if self.is_leap_year() == True and self.new_day == 1:
                # Change day and month if beginning of March and leap year.
                self.new_month = 2
                self.new_day = 29

            elif self.is_leap_year() == False and self.new_day == 1:
                # Change day, month if beginning of March.
                self.new_month = 2
                self.new_day = 28

            else:
                # Change day if not end month.
                self.new_day = self.new_day - 1

        elif (
            days_month_in_date_object == 28
            and self.is_valid_date() == True
            and self.new_month == 2
        ):  # Check if day is beginning of February and year not a leap year
            if self.new_day != 1:
                self.new_day = self.new_day - 1

            elif self.new_day == 1:
                # Change day if not begginning of March and year is not leap year.
                self.new_month = 1
                self.new_day = 31

        elif (
            self.is_leap_year() == True
            and self.is_valid_date() == True
            and self.new_month == 2
        ):  # Check if year is a leap year.

            if self.new_day != 1:
                self.new_day = self.new_day - 1

            elif self.new_day == 1:
                # Change day, month if beginning of February and year is leap year.
                self.new_day = 31
                self.new_month = 1

    def add_n_days(self, n):
        """Changes the calling object so that it 
        represents n calendar days after the date it originally represented.
        """
        for number in range(n):
            self.add_one_day()

    def rem_n_days(self, n):
        """Changes the calling object so that it represents 
        n calendar days before the date it originally represented.
        """

        for number in range(n):
            self.rem_one_day()

    def __eq__(self, other):
        """Returns True if the called object 
        (self) and the argument (other) represent the same calendar date.
        """

        if self.__dict__ == other.__dict__:
            return True
        else:
            return False

    def is_before(self, other):
        """Returns True if the called object represents a calendar date 
        that occurs before the calendar date that is represented by other. 
        """

        if (
            self.new_day < other.new_day
            and self.new_month < other.new_month
            and self.new_year < other.new_year
        ):
            return True

        elif self.new_month < other.new_month and self.new_year == other.new_year:
            return True

        elif (
            self.new_day < other.new_day
            and self.new_month == other.new_month
            and self.new_year == other.new_year
        ):
            return True

        elif self.new_year < other.new_year:
            return True

        else:
            return False

    def is_after(self, other):
        """Returns True if the calling object represents a calendar 
        date that occurs after the calendar date that is represented by other. 
        """

        if (
            self.new_day > other.new_day
            and self.new_month > other.new_month
            and self.new_year > other.new_year
        ):
            return True

        elif self.new_month > other.new_month and self.new_year == other.new_year:
            return True

        elif (
            self.new_day > other.new_day
            and self.new_month == other.new_month
            and self.new_year == other.new_year
        ):
            return True

        elif self.new_year > other.new_year:
            return True

        else:
            return False

    def diff(self, other):
        """Returns an integer that represents the number of days between self and other."""
        copy.deepcopy(other)
        copy.deepcopy(Date)
        days_diff = 0
        if (
            self.new_day == other.new_day
            and self.new_month == other.new_month
            and self.new_year == other.new_year
        ):
            days_diff = 0

        else:
            if self.is_before(other) == True:
                while self.__eq__(other) == False:
                    days_diff += -1
                    self.add_one_day()
                    if self.__eq__(other) == True:
                        break

            elif self.is_after(other) == True:
                while self.__eq__(other) == False:
                    days_diff += 1
                    other.add_one_day()
                    if self.__eq__(other) == True:
                        break

        return days_diff

    def day_of_week(self):
        """Returns a string that indicates the day of the week of the Date 
        object that calls it.
        """
        day_of_week_names = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        known_date = Date(4, 18, 2016)
        days_diff = self.diff(known_date)

        return day_of_week_names[days_diff % 7]


if __name__ == "__main__":
    # print("Works")
    pass
