# for loops do not use pre-defined variables.
# instead, it uses the temporarily defined variables within its loop.

# A dictionary version of vowels3.py
# This is an interactive mode to find the unique vowels entered by the user.


word = input("Provide a word to search for vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u'] # a list

found = {} # defining a dictionary and leave it empty to be filled.


for letter in word:
    if letter in vowels:

for k, v in sorted(found.items()): # invoke items method on the found dict.
    print(k, 'was found', v, 'times(s).')










found = []
for letter in word: # checking the word membership with "in".
    if letter in vowels: # any vowels in word?
        if letter not in found: # if these vowels are not in 'found',
            found.append(letter) # then append the 'letter' to 'found'.
for vowel in found: # using a new for loop variable 'vowel'.
    print(vowel) # then print the 'vowel'.

print(found)
