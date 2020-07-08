küsimine = True
while küsimine == True:
    try:
        number = int(input("Sisesta number jagamise jaoks"))
        print (18/number)
        break
    except ZeroDivisionError:
        print("ära kasuta nulli")
    except ValueError:
        print("see ei ole number")
    finally:
        print("loop complete")