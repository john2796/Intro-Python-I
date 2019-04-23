"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:

 -[x] If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.

 -[x] If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.

 -[x] If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.

 -[x] Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# function that dynamically takes in year and month to print calendar


def calendarFunc(month=datetime.now().month, year=datetime.now().year):
    if month > 13:
        return "Month must be less than 12"
    else:
        return calendar.month(year, month)


def checkType(x):
    if x.isdigit():
        return "type must be a number"


def calendarMonth():
    x = input("Enter calendar.py month [year] :")
    length = x.split(' ')
    print("---- length of list ----", len(length))

    if len(x) == 0 and checkType(x):
        return calendarFunc()
    elif len(length) == 1 and checkType(x):
        month = int(length[0])
        return calendarFunc(month)
    elif len(length) == 2 and checkType(x):
        month = int(length[1])
        year = int(length[0])
        return calendarFunc(month, year)
    else:
        print('Please fix your format for example "2019 4"')


print(calendarMonth())
