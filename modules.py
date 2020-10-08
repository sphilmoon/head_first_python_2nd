# importing a (submodule or function) from standard library (module).
# the function is a part of module.
# multiple modules make a large standard library.
# "Python ships with batteries included."

import os
# print(os.environ) # using an environ attribute.
print(os.getenv('HOME')) # using a getenv function with a specified key word.

# user-friendly of today's date.
import datetime
print(datetime.date.isoformat(datetime.date.today()))

import time
print(time.strftime("%H:%M:%S")) # printing hh/mm/ss in 24-hour string format.
print(time.strftime("%A %p")) # which day? AM or PM?

# escape for encode, unescape for decode using html module.
import html
print(html.escape("The escape function to encode <script>script</script> tag."))
print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))
