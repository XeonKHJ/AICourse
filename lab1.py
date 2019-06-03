#%%
import random


msg = "Hello World"
print(msg)

prize = 0
for i in range(100):
    roll = random.randint(1, 6)
    if roll % 2 == 0:
        prize += roll
    else:
        prize -= 1
    print(prize)