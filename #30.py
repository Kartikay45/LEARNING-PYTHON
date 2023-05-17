import pandas as pd
print(pd.__version__)
# or
import math 

#or

from math import sqrt,floor as sq

#or
from math import * #not recomended

# to display all pakages of that module

import math
print(dir(math))

# importing a made module of mine
# save file as kartik.py

# def welcome():
#     print("you are welcome here")

# kartik="a good boy"   
 
from kartik import welcome,kartik

welcome()
print(kartik)