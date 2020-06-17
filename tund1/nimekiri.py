nimekiri = [100, 36.36, "Arvuti"]

print (nimekiri[-1])

nimekiri.append("lisasin selle juurde")
#print (nimekiri)
nimekiri.insert(0, 8)
print (nimekiri)
nimekiri.pop()
print(nimekiri)

nimekiri[1] = "üks"
print(nimekiri)

if nimekiri[0] < nimekiri[2]:
    print (nimekiri[0]-nimekiri[2])

print (len(nimekiri))

#sisestus = float(input("mingi arv mis nimekirja"))
#nimekiri.append(sisestus)
#print(nimekiri)
nimekiri2 = [5, 7, 1, 4]
nimekiri2.sort()
print (nimekiri2)