"""
Program: Calendar Module - Find the day of  the week
Author: Mulenga Chituta
Description:
This Python program demonstrates the use of the "calendar' module
to determine the day of the week for a given date.

The program reads a date input in the format: MM DD YYYY
and outputs the corresponding day of the week in uppercase letters.

It uses the calendar.weekday(year, month, day) function,
which returns an integer representing the day of the week:
0 = Monday, 1 = Tuesday, ..., 6 = Sunday.

The program then retrieves the corresponding day name from
calendar.day_name[] and converts it to uppercase for display.

Example: Input:
10 11 25

Output:
MONDAY
"""

import calendar

# read date input in the format: MM DD YYY
month, day, year = map(int, input("Enter date (MM DD YYYY): ").split())


# get the weekday number (0 = Monday, 6 = Sunday)
weekday_number = calendar.weekday(year, month, day)

# get the weekday name and convert it to uppercase
weekday_name = calendar.day_name[weekday_number].upper()

# Display the result
print(weekday_name)

                                  

