# defining an 'odds' variable.
# '=' is an assignment operator.
# the others are usual operators.
# you ALWAYS assign values to variables.

from datetime import datetime # from 'module' import 'submodule'.
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute # invoking the function.
# datetime is submodule, today is method, minute is attribute.
# dot notation is used b/w submodule/function-method-attribute.

# a block of code is always indented.
# total two blocks of code.
# in python, this is called "suites" of code instead.
# always indent after using the colon (:).
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")
