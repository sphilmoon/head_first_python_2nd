# for loops do not use pre-defined variables.
# instead, it uses the temporarily defined variables within its loop.
# using a list to avoid any duplicates.

# This is an interactive mode to find the unique vowels entered by the user.

word = input("Provide a word to search for vowels: ")
vowels = ['a', 'e', 'i', 'o', 'u'] # a list
found = [] # starting with an empty list.

for letter in word: # checking the word membership with "in".
    if letter in vowels: # any vowels in word?
        if letter not in found: # if these vowels are not in 'found',
            found.append(letter) # then append the 'letter' to 'found'.
for vowel in found: # using a new for loop variable 'vowel'.
    print(vowel) # then print those vowels.

print(found) # also, print the 'found' to list these vowels.
