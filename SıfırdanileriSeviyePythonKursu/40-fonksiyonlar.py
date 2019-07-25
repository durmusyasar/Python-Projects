def ucgenmi(a,b,hipo):
    toplam = a**2 + b**2
    if toplam == hipo**2:
        print("Bu bir dik üçgendir")
    else:
        print("Değil")



# ucgenmi(3, 4, 5)

##################################

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
    baslangıcBosluk = cap // 2 - 1
    pass

"""
tersSlac(10)
bosluk(20)
slac(5)
satirAtla(10)
bosluk(20)
tersSlac(4)
"""

bosluk(4)
slac(1)
bosluk(0)
tersSlac(1)
satirAtla(1)
#############
bosluk(3)
slac(1)
bosluk(2)
tersSlac(1)
satirAtla(1)
#############
bosluk(2)
slac(1)
bosluk(4)
tersSlac(1)
satirAtla(1)
#############
bosluk(1)
slac(1)
bosluk(6)
tersSlac(1)
satirAtla(1)
#############
bosluk(0)
slac(1)
bosluk(8)
tersSlac(1)
satirAtla(1)
#############3