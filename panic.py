#!/usr/bin/env python3
# transforming the string into another string. 

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# generate "on tap" message to this file using a for loop:
for i in range(4):
    plist.pop()

plist.remove("'")
plist.pop(0)
plist.extend([plist.pop(), plist.pop()]) #swapping the last two letters
# in the order of popping.
plist.insert(2, plist.pop(3)) # inserting the space on the 2nd index location.


# plist.extend("on tap")

# now with the new_phrase:
# defining a new variable for printing as a string.
new_phrase = ''.join(plist) # turning the list into a string.
print(plist) # the modified letter-by-letter list.
print(new_phrase) # printing the string form.
