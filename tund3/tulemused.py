tulemused = {
    "Marko" : 71,
    "Mari-Liis" : 86,
    "Henri" : 62,
    "Sandra" : 91
    }

parimNimi = 0
parimTulemus = 0

for x, y in tulemused.items():
    if y > parimTulemus:
        parimNimi = x
        parimTulemus = y
    else:
        continue
print ("Parim tulemus oli", parimNimi, "ja ta sai", parimTulemus, "punkti")