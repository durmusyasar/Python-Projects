'''while True :
    try :
        ilk_sayi = float(input("ilk sayi gir : "))
        ikinci_sayi = float(input("ikinci sayi : "))
        print(ilk_sayi / ikinci_sayi)
    except ValueError as degisken:
        print(degisken)
        print("Lütfrn harf girmeyiniz")'''

while True :
    try :
        ilk_sayi = float(input("ilk sayi gir : "))
        ikinci_sayi = float(input("ikinci sayi : "))
        print(ilk_sayi / ikinci_sayi)
    except ValueError :
        print("Lütfrn harf girmeyiniz")
    else :
        try :
            print(ilk_sayi / ikinci_sayi)
        except ZeroDivisionError :
            print("Bir sayi sıfıra bölünmez")