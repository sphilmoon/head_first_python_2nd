#!/bin/env python3
word = "bottles" # assigning the value (as a string) to the 'word' variable.

# beer_num is a loop iteration variable.
for beer_num in range(99, 0, -1): # start, stop, step. Counting down from 99.
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.") # total four lines of lyric.
    if beer_num == 1: # if there is only 1 beer remaining, print the below.
        print("No more bottles of beer on the wall.") # end of the songs.
    else: # otherwise, keep itertating the count-down for the next beer.
        new_num = beer_num - 1 # a NEW LOOP ITERATION VARIABLE for updating the quantity of beers remaining.
        if new_num == 1: # until the very last beer.
            word = "bottle" # then use the 'word' variable.
        print(new_num, word, "of beer on the wall.") # part of the else conditiion.
    print() # blank line between each iteration.

# 1. define any variable in string.
# 2. begin the for loop with a new variable that is given a specific repetition.
# 3. embed any neccessary conditions in the for loop to repeat or count down.
# 4. print() for printing the strings.
