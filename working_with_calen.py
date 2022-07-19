import calendar
from time import strftime

#create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY) # sunday will be the day that a week starts
strin = c.formatmonth(2022, 6, 0, 0) #format month in a text string
print(strin)

#create a HTML-formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY) 
strin = hc.formatmonth(2022, 6) 
print(strin)

#loops over the days of month
for i in c.itermonthdays(2022, 6):
    print(i)

#print the days and months in both full and abbreviated form
for name in calendar.month_name: # you can replace . month_name with .month_abbrev
    print(name)
for day in calendar.day_name:      # you can replace . day_name with .day_abbrev
    print(day)

# project
print("Team meeting will be on:")
for i in range(1, 13): # loop over the 12 months of a year
    month_of_year = calendar.monthcalendar(2022, i)
    week1 = month_of_year[0]
    week2 = month_of_year[1]
    if week1[calendar.FRIDAY ]!= 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]
    print(calendar.month_name[i], meetday)


    
    
