ruudustik1 = {"1" : " ", "2" : "8", "3" : " ", "4" : "4", "5" : " ", "6" : "9", "7" : "3", "8" : "6", "9" : " "}
ruudustik2 = {"1" : "2", "2" : "6", "3" : " ", "4" : " ", "5" : " ", "6" : "8", "7" : " ", "8" : " ", "9" : "4"}
ruudustik3 = {"1" : " ", "2" : "7", "3" : " ", "4" : " ", "5" : " ", "6" : "1", "7" : " ", "8" : "2", "9" : " "}
ruudustik4 = {"1" : "6", "2" : " ", "3" : "4", "4" : "8", "5" : " ", "6" : "2", "7" : " ", "8" : "5", "9" : "1"}
ruudustik5 = {"1" : " ", "2" : "1", "3" : "2", "4" : "7", "5" : " ", "6" : "5", "7" : " ", "8" : " ", "9" : "3"}
ruudustik6 = {"1" : " ", "2" : " ", "3" : " ", "4" : "1", "5" : " ", "6" : " ", "7" : "4", "8" : "8", "9" : " "}
ruudustik7 = {"1" : "1", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : "2", "8" : "7", "9" : "6"}
ruudustik8 = {"1" : " ", "2" : "4", "3" : " ", "4" : "2", "5" : " ", "6" : "7", "7" : " ", "8" : " ", "9" : "8"}
ruudustik9 = {"1" : "7", "2" : "2", "3" : "8", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : "5"}

väljakKogu = {
    "1" : ruudustik1,
    "2" : ruudustik2,
    "3" : ruudustik3,
    "4" : ruudustik4,
    "5" : ruudustik5,
    "6" : ruudustik6,
    "7" : ruudustik7,
    "8" : ruudustik8,
    "9" : ruudustik9,
}



def enterNumber(väljakKogu):
    outerLoop = True
    while outerLoop == True:
        print("\n")
        rida = input("Vali rida: ")
        asukoht = input("Vali asukoht: ")
        try:
            r = väljakKogu[rida]
        except:
            print("Ei sobi")
            continue
        for x in r:
            if x == asukoht:
                while True:
                    if r[x] == " ":
                        nr = input("Mis number tuleb: ")
                        kontrollH = Horisontaal(väljakKogu, nr, rida, asukoht)
                        kontrollV = Vertikaal(väljakKogu, nr, asukoht)
                        kontrollKast = kastKontroll(väljakKogu, nr, rida, asukoht)
                        try:
                            if kontrollH == True and kontrollV == True and kontrollKast == True and int(nr)<=9 and int(nr)>0:
                                r[x] = nr
                                outerLoop = False
                                break
                            else:
                                print("Ei sobi1")
                        except:
                            print("Ei sobi2")
                    else:
                        print("Ei sobi3")


            
def printVäljak(väljakKogu):
    counterrida = 0
    for x in väljakKogu.values():
        counterveerg = 0
        if counterrida == 3:
            print ("\n" + "-"*19)
            print("", end='|')
            counterrida = 0
        else:
            print(" ")
            print("", end='|')
        for y in x.values():
            counterveerg += 1
            if counterveerg == 3:
                print (y, sep=' ', end='|')
                counterveerg = 0
            else:
                print (y, sep=' ', end=' ')
        counterrida += 1


def Horisontaal(väljakKogu, nr, rida, asukoht):
    kontroll = True
    r = väljakKogu[str(rida)]
    for x in r:
        if x == asukoht:
            if nr in väljakKogu[str(rida)].values():
                print("see number juba horisontaalselt olemas")
                kontroll = False
    if kontroll == False:
        return False
    else:
        return True

def Vertikaal(väljakKogu, nr, asukoht):
    kontroll = True
    for x in range(9):
        for y in väljakKogu.values():
            for z in y.values():
                if y[asukoht] == nr:
                    kontroll = False
    if kontroll == False:
        print("See number on juba vertikaalselt olemas")
        return False
    else:
        return True

def kastKontroll(väljakKogu, nr, rida, asukoht):
    if int(rida) <= 3:
        if int(asukoht) <=3:
            return kastKontroll2(nr, rida, asukoht)
        elif int(asukoht) >=7:
            return kastKontroll2(nr, rida, asukoht)
        else:
            return kastKontroll2(nr, rida, asukoht)
    elif int(rida) >= 7:
        if int(asukoht) <=3:
            return kastKontroll2(nr, rida, asukoht)
        elif int(asukoht) >=7:
            return kastKontroll2(nr, rida, asukoht)
        else:
            return kastKontroll2(nr, rida, asukoht)
    else:
        if int(asukoht) <=3:
            return kastKontroll2(nr, rida, asukoht)
        elif int(asukoht) >=7:
            return kastKontroll2(nr, rida, asukoht)
        else:
            return kastKontroll2(nr, rida, asukoht)

def kastKontroll2(nr, rida, asukoht):
    kontroll = True
    numbers = []
    counterrida = int(rida)
    counterAsukoht = 0
    for x in väljakKogu.values():
        counter = 0
        for y in x.values():
            counterAsukoht = counterAsukoht + 1
            if counter < 3 and counterrida <= 3 and counterrida >= counterrida-3 and int(asukoht) >= counterAsukoht and int(asukoht) <=9:
                numbers.append(y)
                counter = counter + 1
        counterrida = counterrida + 1
    if nr in numbers:
        kontroll = False
    return kontroll

def victoryCondition(väljakKogu):
    marker = True
    for x in väljakKogu.values():
        if " " in x.values():
            marker = False
        else: 
            continue
    if marker == True:
        return True
    else:
        return False

print("Sudoku mäng")
print("Numbreid saab sisesta nii, et algul valid mis reale, näiteks kui soovid esimesele siis sisestad numbri 1")
print("Pärast seda valid asukoha, need on tähistatud kui numbrid 1 kuni 9")
input("Kui selge, siis vajutada enter")


while victoryCondition(väljakKogu) == False:
    printVäljak(väljakKogu)
    enterNumber(väljakKogu)