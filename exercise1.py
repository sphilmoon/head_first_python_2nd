from datetime import datetime # from 'module' import 'submodule'.
import time
import random

# defining odd minutes using a list.
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

# using a for loop so a variable 'i' can iterate 5 times.
# every suites of code belongs to the for loop.
# overall, print the very current minute first, then wait random seconds
# for identifying the next minute. Doing this for 5 times in total.
for i in range(5):
    right_this_minute = datetime.today().minute # key variable def using module.
    if right_this_minute in odds: # assigning a minute variable to the odds.
        print("A little bit of odd minute.")
    else:
        print("An even minute.")
    wait_time = random.randint(1,60) # def using random module and its function.
    time.sleep(wait_time) # sleep before moving to the next sequence.
