import kontroll

def printVäljak(väljak):
    print (väljak["7"] + "|" + väljak["8"] + "|" + väljak["9"])
    print ("-+-+-")
    print (väljak["4"] + "|" + väljak["5"] + "|" + väljak["6"])
    print ("-+-+-")
    print (väljak["1"] + "|" + väljak["2"] + "|" + väljak["3"])

def uuendaVäljak(väljak, sümbol, positsioon):
    if sümbol == "x":
        väljak[str(positsioon)] = sümbol
    else:
        väljak[str(positsioon)] = sümbol

def võiduKontroll(väljak, käigud, sümbol):
    if (([väljak["1"], väljak["2"], väljak["3"]] == ["x", "x", "x"] or [väljak["1"], väljak["2"], väljak["3"]] == ["o", "o", "o"])
    or ([väljak["4"] and väljak["5"] and väljak["6"]] == ["x", "x", "x"] or [väljak["4"] and väljak["5"] and väljak["6"]] == ["o", "o", "o"])
    or ([väljak["7"] and väljak["8"] and väljak["9"]] == ["x", "x", "x"] or [väljak["7"] and väljak["8"] and väljak["9"]] == ["o", "o", "o"])
    or ([väljak["1"] and väljak["4"] and väljak["7"]] == ["x", "x", "x"] or [väljak["1"] and väljak["4"] and väljak["7"]] == ["o", "o", "o"])
    or ([väljak["2"] and väljak["5"] and väljak["8"]] == ["x", "x", "x"] or [väljak["2"] and väljak["5"] and väljak["8"]] == ["o", "o", "o"])
    or ([väljak["3"] and väljak["6"] and väljak["9"]] == ["x", "x", "x"] or [väljak["3"] and väljak["6"] and väljak["9"]] == ["o", "o", "o"])
    or ([väljak["1"] and väljak["5"] and väljak["9"]] == ["x", "x", "x"] or [väljak["1"] and väljak["5"] and väljak["9"]] == ["o", "o", "o"])
    or ([väljak["3"] and väljak["5"] and väljak["7"]] == ["x", "x", "x"] or [väljak["3"] and väljak["5"] and väljak["7"]] == ["o", "o", "o"])):
        if sümbol == "x":
            print ("võitis mängija x")
            mäng = False
        else:
            print ("võitis mängija o")
            mäng = False
    elif käigud == 9:
        print ("viik")
        mäng = False
    else:
        mäng = True
    return mäng

väljak = {
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9"
}
prevSümbol = None
mäng = True
käigud = 0
while mäng == True:
    while True:
        sümbol = kontroll.sümbol()
        if prevSümbol == sümbol:
            print("Ära tee sohki")
            continue
        else:
            break
    printVäljak(väljak)
    while True:
        positsioon = kontroll.positisioon()
        if väljak[str(positsioon)] == "x" or väljak[str(positsioon)] == "o":
            print("siin juba on sümbol")
            continue
        else:
            break
    uuendaVäljak(väljak, sümbol, positsioon)
    prevSümbol = sümbol
    käigud += 1
    mäng = võiduKontroll(väljak, käigud, sümbol)