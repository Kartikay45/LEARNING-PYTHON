# os module in python

import os
os.mkdir("data")
for i in range(0,100):
    os.mkdir(f"data/day{i+1}")
os.mkdir()

folders=os.listdir("data")
os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")


