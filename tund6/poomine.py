import random
import poomisFunktsioonid

elu = 10
mäng = True
spikkerNimekiri, tühiNimekiri = poomisFunktsioonid.algus()
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
        mäng = poomisFunktsioonid.uuesti()
        if mäng == True:
            spikkerNimekiri, tühiNimekiri = poomisFunktsioonid.algus()
    elif spikkerNimekiri == tühiNimekiri:
        print("Tubli et võitsid")
        mäng = poomisFunktsioonid.uuesti()
        if mäng == True:
            spikkerNimekiri, tühiNimekiri = poomisFunktsioonid.algus()