#slicing strings

string = "Hello Python"
print(string[7:50])
print(string[:])
print(string[2:])
print(string[:8])

#find() finds out the first occurence of a specific substring in a string
fruit = "bananana"
i = fruit.find("na")
print(i)

# LIST 
friends = ["Tien", "Tram", "Anh"] 
for i in range(len(friends)):                   #for friend in friends:
    friend = friends[i]                             #print("Happy birthday:", friend)
    print("Happy birthday:", friend)

#
print(range(4))

#concatenate loops
more_friends = ["Nhien", "Ky", "Linh"]
friendss = friends + more_friends
print(friendss)

#building list
stuff = list()
stuff.append("books")
stuff.append("pen")
print(stuff)

#calculate the average of given numbers
# numlist = list()
# while True:
#     number = input("Enter a number:")
#     if number == "done":
#         break
#     elif number == "q":
#         quit()
#     value = float(number)
#     numlist.append(value)
#     continue
# print("The average is:", float(sum(numlist) / len(numlist)))

#OR

# count = 0
# total = 0
# while True:
#     number2 = input("Enter a number:")
#     if number2 == "done":
#         break
#     value2 = float(number2)
#     count += 1
#     total = total + value2
#     continue
# print("The average is:", float(total / count))

#the relationship of list and string
splitted_string = string.split()
print(splitted_string)
for w in splitted_string:
    print(w)
for ww in splitted_string[0]:
    print(ww)

