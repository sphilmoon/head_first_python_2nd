# for loops do not use pre-defined variables.
# instead, it uses the temporarily defined variables within its loop.

# A dictionary version of vowels3.py
# This is an interactive mode to find the unique vowels entered by the user.


word = input("Provide a word to search for vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u'] # a list

found = {} # defining a dictionary and leave it empty to be filled.

# initialize the each values with keys.
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1 # incrementing the value by one.

for k, v in sorted(found.items()): # invoke items method on the found dict. Using two loop variables.
    print(k, 'was found', v, 'times(s).') # key/values.
