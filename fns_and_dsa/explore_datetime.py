#!/usr/bin/python3
import datetime

def display_current_datetime():
    """function that displays the current date and time."""
    current_date = datetime.datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")


def calculate_future_date():
    """function that calculates a future date from the current date"""
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    num_of_days =  datetime.timedelta(number_of_days)
    current_date = datetime.datetime.now()
    future_date = current_date + num_of_days
    return future_date.strftime("%Y-%m-%d")

print(f'Current date and time: {display_current_datetime()}')
print(f'Future date: {calculate_future_date()}')