#!/usr/bin/env python3

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# generate "on tap" message to this file using a for loop:
# for i in range(4):
    # plist.pop()

# plist.pop(0)
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist[1:3]) # turning the list into a string.
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[-5], plist[-6]])


print(plist) # the modified letter-by-letter list.
print(new_phrase) # printing the string form.

# new_phrase_list = list(new_phrase)

# print(new_phrase_list) # the modified letter-by-letter list.
