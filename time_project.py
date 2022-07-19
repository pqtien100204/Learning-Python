import calendar

def countdays(theyear, themonth, whichday)
print("Which day would you like to count?")

while True:
    try:
        print("0. Monday")
        print("1. Tuesday")
        print("2. Wednesday")
        print("3. Thursday")
        print("4. Friday")
        print("5. Saturday")
        print("6. Sunday")
        print("Or 'exit' to quit")

        theday = input("? ")
        if input == "exit":
            break

        day = int(theday)
        year_string = input("Please enter the year: ")
    # year = int(year_string)
    # if year.isdigit() == False:
    #     print("Please enter a valid year!")
    #     continue
    # else:
        month_string = input("Please enter the month: ")
        month = int(month_string)
        # if month != calendar.month_name():
        #     print("Please enter a valid month !")
        #     continue
        # else: 
        result = countdays(year, month, day)
        print("There are", str(result), "of those day in the year and month specified")
        print("---------------------------")

    except Exception as e:
        print(e)
        print("Sorry, that's not a valid input!")


    



