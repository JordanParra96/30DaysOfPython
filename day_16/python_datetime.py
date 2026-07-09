"""Day 16: 30 Days of python programming"""

# Exercise 1: Get the current date and time
from datetime import datetime

CURRENT_DAY = datetime.now().day
print(f"Current day: {CURRENT_DAY}")

CURRENT_MONTH = datetime.now().month
print(f"Current month: {CURRENT_MONTH}")

CURRENT_YEAR = datetime.now().year
print(f"Current year: {CURRENT_YEAR}")

CURRENT_HOUR = datetime.now().hour
print(f"Current hour: {CURRENT_HOUR}")

CURRENT_MINUTE = datetime.now().minute
print(f"Current minute: {CURRENT_MINUTE}")

CURRENT_TIMESTAMP = datetime.now().timestamp()
print(f"Current timestamp: {CURRENT_TIMESTAMP}")

# Exercise 2: Format the current date and time
CURRENT_DATE_TIME = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print(f"Current date and time: {CURRENT_DATE_TIME}")

# Exercise 3: Change time string to time
TIME_STRING = "5 December, 2019"
date_object = datetime.strptime(TIME_STRING, "%d %B, %Y")
print(f"Date object: {date_object}")
