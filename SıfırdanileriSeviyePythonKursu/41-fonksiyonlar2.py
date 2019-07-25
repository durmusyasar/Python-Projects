def slac(adet):
    for i in range(adet):
        print("/", end = "")

def tersSlac(adet):
    for i in range(adet):
        print("\\", end = "")

def bosluk(adet):
    for i in range(adet):
        print(" ", end = "")

def satirAtla(adet):
    for i in range(adet):
        print()

def paralelKenarUst(cap):
    baslangicBosluk = int(cap//2-1)
    tekrar = baslangicBosluk +1
    for i in range(tekrar):
        bosluk(baslangicBosluk)
        slac(1)
        bosluk(2 * i)
        tersSlac(1)
        satirAtla(1)

def paralelKenarAlt(cap):
    icBosluk = int(cap - 2)
    tekrar = int(cap // 2)
    for i in range(tekrar):
        bosluk(i)
        tersSlac(1)
        bosluk(icBosluk - (i * 2))
        slac(1)
        satirAtla(1)

def paralelKenar(cap):
    paralelKenarUst(cap)
    paralelKenarAlt(cap)

paralelKenarUst(20)