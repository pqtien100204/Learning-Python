from datetime import time        # from the Python standard module of datetime, import time, date and datetime classes(pre-defined functionality)
from datetime import date
from datetime import datetime

#get today's date by the simple today() method from the date class
today = date.today()
print("Today's date is:", today)

#get today's day component
print("Today's day component is:", today.day, today.month, today.year)

#get week's day
print("Today's weekday is:", today.weekday())
days = ["mon", "tue", "wed", "thurs", "fri", "sat", "sun"]
print("Today's weekday is:", days[today.weekday()])

#get today's day and time with the now() method from the datetime class
today_datetime = datetime.now()
print("Today's day and time is:", today_datetime)

#get the current time
time = datetime.time(datetime.now()) #remember the descriptor of datetime.datetime objects(date or time) always need an arg
print("Current time is:", time)
