def asalmi(sayi):
    if (sayi == 1):
        return True
    elif (sayi == 2):
        return True
    else:
        for i in range(2, sayi):
            if (sayi % i == 0):
                return False
        return True

while True:
    sayi = input("Sayi : ")

    if (sayi == "q"):
        break
    else:
        sayi= int(sayi)

        if (asalmi(sayi)):
            print(sayi, "asal bir sayidir")
        else:
            print("Sayi asal değildir")