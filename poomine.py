def sisestaja(sõna):
    nimekiri = []
    for x in sõna:
        nimekiri.append(x)
    return nimekiri

def tühiSisestaja(spikkerNimekiri):
    nimekiri = []
    for x in range(len(spikkerNimekiri)):
        nimekiri.append("_")
    return nimekiri

sõna = input("Palun sisesta sõna")
spikkerNimekiri = sisestaja(sõna)
tühiNimekiri = tühiSisestaja(spikkerNimekiri)

elu = 10
mäng = True
while mäng == True:
    kontroll = True
    print (tühiNimekiri)
    counter = 0
    täht = input("Paku täht")
    for y in spikkerNimekiri:
        if täht == y:
            tühiNimekiri[counter] = täht
            kontroll = False
        counter = counter + 1
    if kontroll == True:
        elu = elu - 1
        print("ei leidnud seda tähte")
        print("elud: ", elu)
    if elud == 0:
        mäng = False
    if spikkerNimekiri == tühiNimekiri:
        print("Tubli et võitsid")
        mäng = False