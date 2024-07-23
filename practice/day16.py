# Day 16: 30 Days of python programming

from datetime import datetime

current = datetime.now()
print("Current day:", current.day)
print("Current month:", current.month)
print("Current year:", current.year)
print("Current hour:", current.hour)
print("Current minute:", current.minute)
print("Current timestamp:", current.timestamp())

print(current.strftime("%m/%d/%Y, %H:%M:%S"))

time = "5 December, 2019"
print(datetime.strptime(time, "%d %B, %Y"))

new = datetime(2025, 1, 1)
print(new - current)

date = datetime(1970, 1, 1)
print(current - date)