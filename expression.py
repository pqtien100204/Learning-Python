import re
text = "Hello halo hahaha lo o o oooooo"
#find == re.serach
if text.find("lo") > 0:
    print("Oh yeah yeah yeah")
if re.search("lo", text):
    print("Oh ho ho ho")

#startswith() VS re.search("^")
if text.startswith("Hel"):
    print("Oh yeah yeah yeah")
if re.search("He", text):
    print("Oh ho ho ho")

#re.findall(): all the matching strings to be extracted into a given variable
textt = "My 2 favorite numbers are 10 and 4 and 2"
y = re.findall('[0-9]+', textt)
print(y)
x = re.findall('[aoeui]+', textt)
print(x)