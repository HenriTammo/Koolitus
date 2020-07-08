def recFun(arv):
    if arv == 1:
        return arv
    else:
        return arv * recFun(arv-1)

arv = int(input("Mis arvu faktoriaali soovid?"))
vastus = recFun(arv)
print (vastus)