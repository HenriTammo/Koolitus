import random

avamine = open("näide.txt", "w")

for x in range(10):
    arv = random.randint(0, 10)
    kontroll = True
    while kontroll == True:
        try:
            avamine.write(arv + "\n")
            kontroll = False
        except TypeError:
            arv = str(arv)
        finally:
            continue

avamine.close()

avamine2 = open("näide.txt", "r")

#print(avamine2.readline())
nimekiri = []
for x in avamine2:
    x = x.strip()
    nimekiri.append(x)
print(nimekiri)
avamine2.close()
