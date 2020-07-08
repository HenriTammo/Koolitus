while True:
    try:
        näide = open("create.txt", "x")
    except FileExistsError:
        print("see fail on juba olemas")
        break
    finally:
        print("loop complete")