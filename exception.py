try:
    answer = input("What should I devide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't devide by zero")
except ValueError as e:
    print("You didn't give me a valid number: ", answer)
finally:
    print("Thank you")
    