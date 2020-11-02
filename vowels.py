# for loops do not use pre-defined variables.
# it uses the temporarily defined variables within its loop.
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milky ways"

for letter in word: # checking the word membership with "in".
    if letter in vowels: # identify any vowels in the word.
        print(letter) # outputting vowels. 
