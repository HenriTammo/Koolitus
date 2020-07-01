import random

def suvaline():
    x = 0
    for x in range(5):
        x = x + random.randint(1, 1000)
    return x

nimekiri = []
for x in range(200):
    nimekiri.append(suvaline())
    
print (nimekiri)