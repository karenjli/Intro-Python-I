"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# if input = 0 => use current month and current year
# if input = 1 number => use input for month and current year
# if input = 2 numbers => use input for both year and month
# if input > 2 numbers => print statement
# date_time object


if len(sys.argv) == 1:
    c = calendar.TextCalendar()
    str = c.formatmonth(datetime.now().year, datetime.now().month)
    print(str)
elif len(sys.argv) == 2:
    c = calendar.TextCalendar()
    str = c.formatmonth(datetime.now().year, int(sys.argv[1]))
    print(str)
elif len(sys.argv) == 3:
    c = calendar.TextCalendar()
    str = c.formatmonth(int(sys.argv[2]), int(sys.argv[1]))
    print(str)
else:
    print("Month and year are required for the calendar to print.")


# print(len(sys.argv))

# user = input("14_cal.py month [year]")
