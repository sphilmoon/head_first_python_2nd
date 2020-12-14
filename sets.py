# sets start with curly brace, just like dictionaries.
# sets DO NOT identify key/value pairs. Also, no insertion order.
# it removes any duplicates. Printing only the unique letters.
# no colons, only commas.

# no duplicates in sets.
vowels = {'i', 'e', 'e', 'o', 'u', 'e', 'a', 'o', 'i'}
print(vowels)

# another way of assigning a new set object to a variable.
vowels2 = set('aeiou')
word = 'hello'

# union function.
# vowels2 + word variables.
u = vowels2.union(set(word)) # converting the word value into a set of letter.
print(u)

# alphabetically sorting the u variable into a list.
u_list = sorted(list(u))
print(u_list)

# difference function.
# vowels2 - word variables.
d = vowels2.difference(set(word))
print(d) # printing objects that are not in set(word)

# intersection function.
# printing the objects that are also in the set(word)
i = vowels2.intersection(set(word))
print(i)
