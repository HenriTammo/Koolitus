väljakKogu = {}
sõna = "ruudutsik"

for x in range(10):
    sõnaTäis = sõna + str(x + 1)
    sõnastik = {}
    for x in range(10):
        sõnastik[str(x+1)] = x+1
    väljakKogu[sõnaTäis] = sõnastik
print(väljakKogu)