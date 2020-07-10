ruudustik1 = {"a" : "1", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}
ruudustik2 = {"a" : " ", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}
ruudustik3 = {"a" : " ", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}
ruudustik4 = {"a" : " ", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}
ruudustik5 = {"a" : " ", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}
ruudustik6 = {"a" : " ", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}
ruudustik7 = {"a" : " ", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}
ruudustik8 = {"a" : " ", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}
ruudustik9 = {"a" : " ", "b" : " ", "c" : " ", "d" : " ", "e" : " ", "f" : " ", "g" : " ", "h" : " ", "i" : " "}

väljakKogu = {
    "ruudustik1" : ruudustik1,
    "ruudustik2" : ruudustik2,
    "ruudustik3" : ruudustik3,
    "ruudustik4" : ruudustik4,
    "ruudustik5" : ruudustik5,
    "ruudustik6" : ruudustik6,
    "ruudustik7" : ruudustik7,
    "ruudustik8" : ruudustik8,
    "ruudustik9" : ruudustik9,
}

counterrida = 0


rida = input("vali rida")
asukoht = input("vali asukoht")
r = väljakKogu[rida]
print(r)
for x in r:
    print(x)
    if x == asukoht:
        nr = int(input("mis number tuleb"))
        r[x] = nr

for x in väljakKogu.values():
    counterveerg = 0
    if counterrida == 3:
        print ("\n" + "-"*20)
        counterrida = 0
    else:
        print("\n")
    for y in x.values():
        counterveerg += 1
        if counterveerg == 3:
            print (y, sep=' ', end='|')
            counterveerg = 0
        else:
            print (y, sep=' ', end=' ')
    counterrida += 1