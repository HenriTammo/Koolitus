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
    while True:
        try:
            küsimus = input("Kas soovid uuesti mängida(y/n)")
            if küsimus == "y":
                mäng = True
                break
            elif küsimus == "n":
                mäng = False
                break
        except ValueError:
            print("y/n peab olema")
        finally:
            continue
    return mäng

def algus():
    avamine = open("sõnad.txt", "r", encoding="UTF-8")
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