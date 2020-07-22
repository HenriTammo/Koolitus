ruudustik1 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik2 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik3 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik4 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik5 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik6 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik7 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik8 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik9 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik10 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}

väljakKogu1 = {
    "0" : ruudustik1,
    "1" : ruudustik2,
    "2" : ruudustik3,
    "3" : ruudustik4,
    "4" : ruudustik5,
    "5" : ruudustik6,
    "6" : ruudustik7,
    "7" : ruudustik8,
    "8" : ruudustik9,
    "9" : ruudustik10
}

ruudustik11 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik12 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik13 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik14 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik15 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik16 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik17 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik18 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik19 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik20 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}

väljakKogu2 = {
    "0" : ruudustik11,
    "1" : ruudustik12,
    "2" : ruudustik13,
    "3" : ruudustik14,
    "4" : ruudustik15,
    "5" : ruudustik16,
    "6" : ruudustik17,
    "7" : ruudustik18,
    "8" : ruudustik19,
    "9" : ruudustik20
}
legend1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
legend2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def printVäljak(väljakKogu):
    print (" ", end= "|")
    for x in range (len(legend1)):
        print (legend1[x], end= "|")
    print ("")
    counter = 0
    for x in väljakKogu.values():
        print ("-"*22)
        print (legend2[counter], end= "")
        print ("", end= "|")
        for y in x.values():
            print (y, end= "|")
        print("")
        counter += 1

def laevadePaigutamine(väljakKogu):
    printVäljak(väljakKogu)
    outerloop = True
    counter = 1
    while outerloop == True:
        for x in range(counter):
            print ("Paiguta ühene laev mängija")
            rida = input("Vali rida")
            asukoht = input("Vali asukoht")
            try:
                horisontaal = väljakKogu[rida]
            except:
                print ("ei sobi")
                continue
            for x in horisontaal:
                if x == asukoht:
                    while True:
                        if horisontaal[x] == " ":
                            horisontaal[x] = 0
                            outerloop = False
                            printVäljak(väljakKogu)
                            break
    return counter
                        
def rünnak(omaVäljak, vastaseVäljak, elud):
    outerloop = True
    while outerloop == True and elud>0:
        printVäljak(omaVäljak)
        print ("Mis asukohta ründad")
        rida = input("Vali rida")
        asukoht = input("Vali asukoht")
        try:
            horisontaalOma = omaVäljak[rida]
            horisontaalVastane = vastaseVäljak[rida]
        except:
            print ("ei sobi")
            continue
        for x in horisontaalVastane:
            if x == asukoht:
                while True:
                    if horisontaalVastane[x] == 0:
                        horisontaalVastane[x] = " "
                        if horisontaalOma[x] == 0:
                            print("pihtas aga ei asenda sümbolit sest oma laev seal")
                        else:
                            print("pihtas")
                            horisontaalOma[x] = "+"
                        elud = elud -1
                        uuesti = True
                        break
                    elif horisontaalVastane[x] == " ":
                        if horisontaalOma[x] == 0:
                            print("mööda aga ei asenda sümbolit sest oma laev seal")
                        else:
                            print("mööda")
                            horisontaalOma[x] = "x"
                        uuesti = False
                        break
        if uuesti == False:
            outerloop = False
    return elud                       


print ("Tere tulemast laevadepommitamise mängu.")
print ("Igal mängijal on kokku kümme laeva.")
print ("Neli ühe ruudulist laeva, kolm kaheruudulist laeva, kaks kolmeruudulist laeva ja üks neljaruuduline laev.")
print ("Laevade paigutamine toimub suurimaist väiksemateni sinu valitud ruutudele.")
print ("\n")
print ("Mängija 1")
elud1 = laevadePaigutamine(väljakKogu1)
print ("\n")
print ("Mängija 2")
elud2 = laevadePaigutamine(väljakKogu2)


while True:
    elud2 = rünnak(väljakKogu1, väljakKogu2, elud2)
    if elud2 == 0:
        print("mängija1 võitis")
        break
    elud1 = rünnak(väljakKogu2, väljakKogu1, elud1)
    if elud1 == 0:
        print("mängija2 võitis")
        break


