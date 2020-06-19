import random

suvalisedArvud = []
counter = 1000
while counter > 0:
    suvalisedArvud.append(random.randint(0, 100))
    counter = counter - 1
#genereerimine tehtud
#alustan sorteerimisega

maksimum = 0
loendur = 0
for number in suvalisedArvud:
    if number >= maksimum:
        if number == maksimum:
            loendur = loendur + 1
        else:
            loendur = 1
            maksimum = number
    else:
        continue
print ("Suurim number on", maksimum, "ja seda esines", loendur, "korda")