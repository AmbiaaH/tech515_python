# import random
# import math
#
# print(random.random()) #between 0 - 1
# print(random.randrange(1, 10)) #use randrange() function to set a range of numbers
#
# num_float = 2.6
# print(math.ceil(num_float))
# print(math.floor(num_float))
# print(math.pi)
#
# # gives us remainder of the 2 values
# # 5 can't go into 1, so the remainder is 1
# print(f"Remainder from 1/5: {math.remainder(1, 5)}")


# import os
#
# # returns our current working directory
# working_directory = os.getcwd()
# print(f"Current working directory: {working_directory}")
#
# username = os.environ.get('USERNAME') or os.environ.get('USER')
# print(f"The current user is: {username}")
#
# cpu_cores = os.cpu_count()
# print(f'Total CPU cores: {cpu_cores}')
#
# # change directory - must exist
# # os.chdir("<folder_name>")
#
# # make a new directory
# # os.mkdir("<folder_name>")

#sys module to get info from python interpreter

# import sys
# # gives us the current paths important to the Python interpreter
# print(f"Current path: {sys.path}")
# print(sys.version)

# import datetime
# # gives us today's date
# print(f"Today's date: {datetime.date.today()}")

import builtins

for name in dir(builtins):
    if name[0].islower():
        print(name)