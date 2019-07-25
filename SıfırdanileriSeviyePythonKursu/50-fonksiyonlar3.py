def toplama(a,b,c):
    print("Toplamları",a+b+c)

toplama(3,4,5)

def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi == 0 or sayi == 1):
        print("Faktöriyel : ",faktoriyel)
    else:
        while (sayi >= 1):
            faktoriyel *= sayi
            sayi -= 1
        print("Faktöriyel : ",faktoriyel)

faktoriyel(10)

def toplama2 (a,b,c):
    return a + b + c

def ikiylecarp (a):
    return a * 2

def uclecarp (a):
    return a * 3

def dordebol (a):
    return a / 4

toplam = toplama2(3,4,5)
print(ikiylecarp(toplam))
print(uclecarp(toplam))
print(dordebol(toplam))