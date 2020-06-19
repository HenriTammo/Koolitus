nimekiri = [1, 2, 3]

sisestus = int(input("Paku nimekirja pikkust"))

if len(nimekiri) > 0:
    if sisestus == len(nimekiri):
        print ("arvasid ära")
    else:
        print("ei arvanud ära")