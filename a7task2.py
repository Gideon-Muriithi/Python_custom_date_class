# a7task2.py - Assignment 7, Task 2
#
# Create Date objects according to Date Class template and use the objects in client code.
#

from a7task1 import Date


def options_expiration_days(year):
    """Returns a list of all of the Dates on which options expire during a calendar year."""
    accumulater_pattern = []

    for mm in range(13):
        for days in range(32):
            date_obj = Date(mm, days, year)
            if (
                date_obj.new_day >= 15
                and date_obj.new_day <= 21
                and date_obj.new_month > 0
                and date_obj.is_valid_date()
            ):
                if (
                    date_obj.day_of_week() == "Friday"
                    and date_obj not in accumulater_pattern
                ):
                    accumulater_pattern.append(date_obj)

    return accumulater_pattern


def market_holidays(year):
    """Returns a list of the Dates of all market holidays for a given year."""
    accumulater_pattern = []
    for mm in range(13):
        for days in range(32):
            date_obj = Date(mm, days, year)
            if date_obj.is_valid_date():
                if (
                    date_obj.new_month == 1
                    and date_obj.day_of_week() != "Sunday"
                    and date_obj.new_day == 1
                ):
                    print(
                        "New Year's Day is observed on",
                        date_obj.day_of_week(),
                        date_obj,
                    )
                    accumulater_pattern.append(date_obj)

                elif (
                    date_obj.new_month == 1
                    and date_obj.day_of_week == "Sunday"
                    and date_obj.new_day == 1
                ):
                    print(
                        "New Year's Day is observed on",
                        date_obj.day_of_week(),
                        date_obj.add_one_day(),
                    )
                    accumulater_pattern.append(date_obj)

                if (
                    date_obj.new_day >= 15
                    and date_obj.new_month == 1
                    and date_obj.new_day <= 21
                ):
                    if date_obj.day_of_week() == "Monday":
                        print(
                            "Martin Luther King Day is observed on",
                            date_obj.day_of_week(),
                            date_obj,
                        )
                        accumulater_pattern.append(date_obj)

                if (
                    date_obj.new_day >= 15
                    and date_obj.new_month == 2
                    and date_obj.new_day <= 21
                ):
                    if date_obj.day_of_week() == "Monday":
                        print(
                            "President's Day is observed on",
                            date_obj.day_of_week(),
                            date_obj,
                        )
                        accumulater_pattern.append(date_obj)

                if date_obj.new_day >= 22 and date_obj.new_month == 5:
                    if date_obj.day_of_week() == "Monday":
                        print(
                            "Memorial Day is observed on",
                            date_obj.day_of_week(),
                            date_obj,
                        )
                        accumulater_pattern.append(date_obj)

                if (
                    date_obj.new_month == 7
                    and date_obj.day_of_week() != "Sunday"
                    and date_obj.new_day == 4
                ):
                    print(
                        "Independence Day is observed on",
                        date_obj.day_of_week(),
                        date_obj,
                    )
                    accumulater_pattern.append(date_obj)

                elif (
                    date_obj.new_month == 7
                    and date_obj.day_of_week == "Sunday"
                    and date_obj.new_day == 4
                ):
                    print(
                        "Independence Day is observed on",
                        date_obj.day_of_week(),
                        date_obj.add_one_day(),
                    )
                    accumulater_pattern.append(date_obj)

                if (
                    date_obj.new_month == 9
                    and date_obj.new_day <= 1
                    and date_obj.day_of_week() != "Monday"
                ):
                    print(
                        "Labor Day is observed on", date_obj,
                    )
                    accumulater_pattern.append(date_obj)

                if (
                    date_obj.new_month == 11
                    and date_obj.new_day >= 22
                    and date_obj.day_of_week() == "Thursday"
                ):
                    print(
                        "Thanksgiving Day is observed on",
                        date_obj.day_of_week(),
                        date_obj,
                    )
                    accumulater_pattern.append(date_obj)

                if (
                    date_obj.new_month == 12
                    and date_obj.day_of_week() != "Sunday"
                    and date_obj.new_day == 25
                ):
                    print(
                        "Christmas Day is observed on",
                        date_obj.day_of_week(),
                        date_obj,
                    )
                    accumulater_pattern.append(date_obj)

                elif (
                    date_obj.new_month == 12
                    and date_obj.day_of_week == "Sunday"
                    and date_obj.new_day == 25
                ):
                    print(
                        "Christmas Day is observed on",
                        date_obj.day_of_week(),
                        date_obj.add_one_day(),
                    )
                    accumulater_pattern.append(date_obj)

    return accumulater_pattern
