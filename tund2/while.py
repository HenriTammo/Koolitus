x = 10
nimekiri = []
while x > 1:
    x = x - 1
    nimekiri.append(x)
print (nimekiri)

sisestus = input("ruut või kolmnurk")
kontroll = True
while kontroll == True:
    if sisestus == "ruut":
        break
    elif sisestus == "kolmnurk":
        break
    else:
        sisestus = input("ruut või kolmnurk")
        continue