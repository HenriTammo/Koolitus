avamine = open("sõnad.txt", "r", encoding="UTF-8")

nimekiri = []
nimekiriNr= []
for x in avamine:
    sõnad = x.strip()
    sõnad = sõnad.split(" ")
    for y in range(len(sõnad)):
        nimekiri.append(sõnad[y])


for x in nimekiri:
    counter = 0
    for y in range(len(nimekiri)):
        if x == nimekiri[y]:
            counter = counter + 1
    nimekiriNr.append(counter)
print(nimekiriNr)

for x in range(len(nimekiri)):
    print (nimekiri[x], nimekiriNr[x])
