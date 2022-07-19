from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta # time delta is a scan of time, it's not a particular date/time, it's a period of time

#create and print a timedelta
print(timedelta(days=35, hours=7, minutes=32, seconds=37))

#calculate when will it be a year from now
now = datetime.now()
print("Today day is:", now)
print("A year from now will be:", str(now + timedelta(days=365)))

#create a timedelta that uses more than one arg. calculate the period of time between now and a point in the future
print("In two weeks and 3 days it will be:", str(now + timedelta(weeks=2, days=3)))

#calculate a mock of time in the past a week from now
print("One week ago it was:", (now - timedelta(weeks=1)).strftime("%A %B %d, %Y"))

#how long it is from now to the April Fool day
today = date.today()
fool_day = date(today.year, 4, 1)
if today > fool_day:
    time_passed = fool_day - today
    print("This year's April Fool's day has gone for", time_passed)
    #fool_day = fool_day.replace(year = today.year +1)
next_fool_day = date(today.year + 1, 4, 1) # instead of specifying a new var, you can reset the fool_day var by: fool_day = fool_day.replace(years = today.year +1)
time_until = next_fool_day - today
print("There will be", time_until, "left until the next April Fool's day")


