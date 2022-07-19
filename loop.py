def main():
    x = 5
# while loop
    while(x >= 0):
        print(x)
        x = x - 1
# for loop is a definite loop which iterate through the members of a set
    for x in range(5, 10): #for x in [5, 6, 7, 8, 9]
        print(x)
    
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

# use break and continue in loop
    for x in range(5, 10):
        if x == 7:
            break
        if x % 2 == 0:
            continue
        print(x)

# use the enumerate() to get index
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    for ind, d in enumerate(days):
        print(d, ind)


main()

#while is sometimes the indefinite loop if it's condition is True, or it could iterate until it reaches the condition => it stop.
n = 0
# while True:                               while n < 3:
#     if n == 3:                            print(n)
#         break                             n += 1
#     print(n)                              continue
#     n = n + 1

#find the smallest value
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

#for loop
zork = 0
print("Before:", zork)
for thing in range(5, 10):
    zork += 1     #can try: zork = zork + thing
    print(zork, thing)
print("After:", zork)

#finding avg in a loop
count = 0
sum = 0
for value in [45, 67, 7, 2, 123, 35, 64]:
    count += 1
    sum = sum + value #gradually adding up 
    print(count, sum, value)
print("The average is:", sum / count)

#filtering in a loop
for something in range(5, 20):
    if something > 12:
        print("These are large values:", something)

#search using boolean variable
find_something = False
for sth in [23, 34, 35, 232, 458, 853, 590]:
    if sth > 250:
        find_something = True
    print(find_something, sth)

#0 == 0.0 true
#0 is 0.0 false

#loop through string
string = "banana"
index = 0
count = 0
while index < len(string):
    letter = string[index]   #this is the same as: for letter in string:
    print(index, letter)
    index += 1
    if letter == "a":
        count += 1
    print("Count 'a':", count)
