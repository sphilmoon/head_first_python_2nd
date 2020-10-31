# using [] for to select specific slices from the list.
# un update from marvin.py

paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char) # single tab.
print()
for char in letters[-7:]:
    print('\t'*2, char) # double tab.
print()
for char in letters[12:20]:
    print('\t'*3, char) # triple tab.
print()
