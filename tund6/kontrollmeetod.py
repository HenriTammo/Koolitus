def sisestus(käigud):
        kontroll = True
        while kontroll == True:
            try:
                kasutaja = int(input("Kas kivi(0), käärid(1) või paber(2)"))
                käik = käigud[kasutaja]
                kontroll = False
            except ValueError:
                print("palun sisesta number(int)")
            except IndexError:
                print("number 0 kuni 2 palun")
            finally:
                continue
        return käik