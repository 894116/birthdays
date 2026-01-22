#! /usr/bin/env python3

from birthdays import return_birthday, add_birthday_entry

return_birthday('Albert Einstein')
return_birthday('Alan Turing')

add_birthday_entry ('Erling Haaland', '07/21/2000')
add_birthday_entry ('Albert Gore', '03/31/1948')
add_birthday_entry('Elizabeth Bowes-Lyon', '08/04/1900')

from birthdays import people_leap_year
print("People born in a leap year:", people_leap_year())

from birthdays import people_leap_year_calendar
print("People born in a leap year (calendar):", people_leap_year_calendar())