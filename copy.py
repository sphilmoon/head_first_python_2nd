first = [1, 2, 3, 4, 5]
print(first)

second = first # copying first to second.
print(second)

second.append(6)
print(second)

print(first) # new object is also appended to the first.
print("")

third = second.copy() # this allows to leave the second intact as copying it.
third.append(7) # manipulating the copyied variable with append function.

print(third)
print(second)

# start, stop, step.
print(third[7::-2]) # from 7th to 0th every second letter, inclusively.

print('phil\'s book') # use \ before the single quote to use it in this case.
