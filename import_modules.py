import math
rads = math.radians(90)
print(rads)

import datetime
today = datetime.date.today()
print(today)

import calendar
print(calendar.isleap(2017))

import random
subjects = ['Japanese', 'Arts', 'Chemistry', 'English', 'CompSci', 'Math']
random_subject = random.choice(subjects)
print(random_subject)

import os
print(os.getcwd())
print(os.__file__)
