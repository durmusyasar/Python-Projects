def anafonksiyon(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def çarpma(*args):
        carp = 1
        for i in args:
            carp *= i
        return carp

    if (islem_adi == toplama):
        return toplama
    else:
        return çarpma

fonk = anafonksiyon("toplama")
print(fonk(1,2))

def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def anafonksiyon(func1,func2,func3,func4,islem_adı):
    if islem_adı == "toplama":
        print(func1(1,2))
    elif islem_adı == "cıkarma":
        print(func2(2,3))
    elif islem_adı == "carpma":
        print(func3(3,4))
    elif islem_adı == "bolme":
        print(func4(4,1))
    else :
        print("Geçersiz işlem....")

anafonksiyon(toplama,cıkarma,carpma,bolme,"toplama")