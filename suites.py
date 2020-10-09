# levels of indentation can demarcate embedded suites.

from datetime import datetime

today = datetime.today()

if today == 'Saturday':
    print('Party time!!!')
elif today == 'Sunday':
    if condition == 'Hangover':
        print('Have some cuppa, and rest.')
    else:
        print('Take a rest.')
else:
    print('Werk, werk, werk says Rihanna.')
