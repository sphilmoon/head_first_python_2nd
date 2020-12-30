# tuples are surrounded by ().
# tuples are immutable, CAN'T change.

vowels = ('a', 'e', 'i', 'o', 'u') # () indicating a tuple.
print(vowels)
print(type(vowels))

# Every string needs a comma b/w the ().
use_comma_for_tuple = ('python',) # a comma indicates tuple, NOT string.
print(type(use_comma_for_tuple))

# adding a new variable in existing <class 'tuple'> will cause an error. 
'''
vowels[2] = 'W'
print(vowles)

Traceback (most recent call last):
  File "tuples.py", line 12, in <module>
    vowels[2] = 'W'
TypeError: 'tuple' object does not support item assignment
''' 