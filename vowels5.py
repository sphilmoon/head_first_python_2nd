word = input("Provide a word to search for vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u'] # a list

found = {} # defining a dictionary and leave it empty to be filled.

# setdefault method avoid spending time to initialize all the rows.
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0) # setdefault method to avoid KeyError message. 
        found[letter] += 1 # incrementing the value by one.

for k, v in sorted(found.items()): # invoke items method on the found dict. Using two loop variables.
    print(k, 'was found', v, 'times(s).') # key/values.
