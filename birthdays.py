
"""
This module contains a dictionary of some famous people's birthday and utility functions to print available names and retrieve a birthday.
"""

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    """Print all the available name in the dictionary"""
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    """Print the birthday of the given person if present in the dictionary"""
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))


def add_birthday_entry(name, birthday):
    """Add a new entry to the birthday dictionary"""
    birthdays[name] = birthday


def people_leap_year():
    """Return the names of the people who are born in a leap years"""

    leap_year_people = []
    for name, date in birthdays.items():
        year = int(date.split("/")[-1])
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            leap_year_people.append(name)

    return leap_year_people

import calendar

def people_leap_year_calendar():
    """Return the names of the people who are born in a leap years using the calendar module  """
    leap_people = []
    for name, date in birthdays.items():
        year = int(date[-4:])
        if calendar.isleap(year):
            leap_people.append(name)
    return leap_people