from ast import Or
from datetime import datetime

now = datetime.now()

#%y/%Y %d(day in month) | %b/%B month %a/%A weekday
print(now.strftime("The current year is: %Y.")) #the strftime () method takes one or more format codes as an argument and returns a formatted string based on it
            #OR
curr_year = now.strftime("%y %Y")
print("The current year is:", curr_year)
print(now.strftime("%A, %B %d, %Y"))

#%c- locale date and time | %x- locale date %X- locale time
print("Current locale date and time is:", now.strftime("%c"))
print("Current locale date is:", now.strftime("%x"))
print("Current locale time is:", now.strftime("%X"))

#%I %H - 12/24 hour | %M minute | %S second | %p locale AM/PM
print(now.strftime("24-hour time is %H:%M:%S %p"))
print(now.strftime("12-hour time is %I:%M:%S %p"))