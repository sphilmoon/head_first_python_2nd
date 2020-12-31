# A set version of vowels3.py, which is considerably simpler.

word = input("Provide a word to search for vowels: ")
vowels = set("aeiou") # new set of vowels.
found = vowels.intersection(set(word)) # reports any common objects found.
print(found) # Since I'm using the set, the output will be in a {}.

