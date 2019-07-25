def fonksiyon(*args): # istediğiniz sayıda argüman gönderebiliyoruz
    print(args)
    for i in args:
        print(i)

fonksiyon(1,2,3,4,5,6) 

def fonksiyon2(isim, *args):
    print("İsim: ",isim)
    print("-------")
    for i in args:
        print(i)

fonksiyon2("Durmuş",1,2,3,4,5,6)



def fonksiyon3(**kwarks):# argümanlara isim vererek göndermemizi sağlar
    print(kwarks)

fonksiyon3(isim="Durmuş",soyisim="YAŞAR", numara=314040)

def fonksiyon4(**kwarks):
    for i,j in kwarks.items():
        print("Argüman ismi",i,"Argüman Değeri",j)

fonksiyon4(isim="Durmuş",soyisim="YAŞAR", numara=314040)


def fonksiyon5(*args, **kwarks):
    for i in args:
        print(i)
    print("-----------------")
    for i, j in kwarks.items():
        print(i, j)

fonksiyon5(1,2,3,4,5,isim="Durmuş",soyisim="YAŞAR", numara=314040)


def fonksiyon6():
    def fonksiyon7():
        print("Fonksiyon 7")
    fonksiyon7()
    print("Fonksiyon 6")

fonksiyon6()

def fonksiyon8(*args):
    def toplama(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(toplama(args))

fonksiyon8(2,4,5,7,65,3)