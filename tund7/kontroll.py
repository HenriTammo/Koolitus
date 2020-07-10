def sümbol():
    kontroll = True
    while kontroll == True:
        sümbol = input("kas x või o")
        if sümbol == "x" or sümbol == "o":
            kontroll = False
        else:
            print("vale sisestus")
    return sümbol
def positisioon():
    kontroll = True
    while kontroll == True:
        positsioon = int(input("Mis kohta soovid")) #saab ka tavalise inputiga teha
        if positsioon > 0 and positsioon < 10:
            kontroll = False
        else:
            print("vale sisestus")
    return positsioon