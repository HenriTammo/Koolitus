kontroll = True
while kontroll == True:
    for x in range(100):
        print("mängin")
    sisestus = input("uuesti jah/ei")
    if sisestus == "jah":
        continue
    else:
        kontroll = False