sisestus = input ("Kas ruut või kolmnurk")
if sisestus == "ruut":
    number = float(input("Sisesta ruudu külg"))
    pindala = number**2
    print (pindala)
elif sisestus == "kolmnurk":
    number1 = float(input("Sisesta kolmnurga esimene külg"))
    number2 = float(input("Sisesta kolmnurga teine külg"))
    pindala = (number1*number2)/2
    print (pindala)