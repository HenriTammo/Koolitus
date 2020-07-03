tähestik = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "š", "t", "u", "x", "y", "z", "ž", "w", "õ", "ö", "ä", "ü", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sisestus = input("Sisesta tekst")
algneTekst = list(sisestus)
lõplikTekst = []

limiit = len(tähestik)
for x in algneTekst:
    for y in range(limiit):
        if x == tähestik[y]:
            if y+3 > limiit-3:
                limiit = limiit + 3
                üleminek = y + 3
                vahe = limiit - üleminek
                lõplikTekst.append(tähestik[vahe])
            else:
                lõplikTekst.append(tähestik[y+3])
print(lõplikTekst)