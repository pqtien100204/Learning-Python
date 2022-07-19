#tuples
x = ("Python", "JS", "PHP")
print(x[0])
for iter in x:
    print(iter)
# x[0] = "SQL"
# print(x)

#tuples VS lists VS strings
#tuples and strings don't allow user to alter the content which is the opposite of list
abc = "ABC"
print(abc[1])
# abc[0] = "D"
# print(abc)

list = ["1thing", "2thing", "3thing"]
print(list[2])
list[0] = "4thing"
print(list)

#tuple can act as a all-in-one assignment statement
(tu, ple) = ("value1", 2)
print(ple)

#dictionary and tuples
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i) #this is a tuple from the d dictionary

t = d.items()
print(t)

#sorted() : sort dictionary(item()) based on the key
sort = sorted(d.items())
print(sort)
for k,v in sort:
    print(k, v)
#way to sort dictionary(item()) based on values.

tmp = []     #declare a list in this way instead of tmp = list()
for ke, va in d.items():
    tmp.append( (va, ke) ) #you switch the position. remember to group the 2 arg into 1 arg when using append
print(tmp)
sort2 = sorted(tmp, reverse=True)
print(sort2)

#project: count the 10 most highly-encountered words in a given text
print("Enter a line of text")
text = input("")
text_words = text.split(" ")
count_words = dict()
print(text_words)
for word in text_words:
    count_words[word] = count_words.get(word, 0) + 1
    # if word not in count_words:
    #     count_words[word] = 1
    # else:
    #     count_words[word] += 1
print(count_words)

print( sorted( [ (v, k) for k,v in count_words.items() ], reverse=True )) # this is called the list comprehnsion which is the shortened form of all the code lines below
#or
reverse_list = []
for keey, vaal in count_words.items():
    reverse_list.append((vaal, keey))
print(reverse_list)
sorted_result = sorted(reverse_list, reverse=True)
print(sorted_result[:3])