import random

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

def uuesti():
    küsimus = input("Kas soovid uuesti mängida(y/n)")
    if küsimus == "y":
        mäng = True
    else:
        mäng = False
    return mäng

def algus():
    avamine = open("tund4\poomine.txt", "r", encoding="UTF-8")
    suvaline = random.randint(0, 9)
    lugeja = 0
    for x in avamine:
        if lugeja == suvaline:
            sõna = x.strip()
            lugeja = lugeja + 1
        else:
            lugeja = lugeja + 1
    spikkerNimekiri = sisestaja(sõna)
    tühiNimekiri = tühiSisestaja(spikkerNimekiri)
    avamine.close()
    return spikkerNimekiri, tühiNimekiri

elu = 10
mäng = True
spikkerNimekiri, tühiNimekiri = algus()
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
    if elu == 0:
        mäng = uuesti()
        if mäng == True:
            spikkerNimekiri, tühiNimekiri = algus()
    elif spikkerNimekiri == tühiNimekiri:
        print("Tubli et võitsid")
        mäng = uuesti()
        if mäng == True:
            spikkerNimekiri, tühiNimekiri = algus()
