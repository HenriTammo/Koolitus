import random
sõnastik = {
    "õun" : random.randint(0, 5),
    "pirn" : 0.15,
    "apelsin" : "otsas"
    }

#print(sõnastik)
#for x in sõnastik:
    #print(x)
    
#for x in sõnastik.values():
    #print(x)

for x, y in sõnastik.items():
    print(x, y)
    
sõnastik["apelsin"] = 0.2

sõnastik["kurk"] = 0.15
sõnastik.pop("pirn")
print(sõnastik)
