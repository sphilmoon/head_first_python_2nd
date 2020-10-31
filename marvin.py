# using a for loop to assing the letters one at a time.
# aka printing each letter per line. 

paranoid_android = 'Marvin\'s note' # assigning a string to a variable.
letters = list(paranoid_android) # then turn the string into a list.
for char in letters:
    print('\t', char) # using the tab \t character.
