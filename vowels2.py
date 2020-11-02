# for loops do not use pre-defined variables.
# it uses the temporarily defined variables within its loop.
# using a list to avoid any duplicates.

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milky ways"
found = []
for letter in word: # checking the word membership with "in".
    if letter in vowels: # any vowels in word?
        if letter not in found: # if these vowels are not in 'found',
            found.append(letter) # append these vowels to 'found'.
for vowel in found: # using a new for loop variable 'vowel'.
    print(vowel) # then print those vowels.

print(found)
