''' izinli_karakterler = "0123456789"
while True:
    hata = 0
    sayi1 = input("Sayi gir :")
    sayi2 = input("Sayi gir : ")

    for karakter in sayi1:
        if karakter not in izinli_karakterler:
            print("Harf girilemez")
            hata = 1;
            break
    for karakter in sayi2:
        if karakter not in izinli_karakterler:
            print("Harf girilemez")
            hata = 1;
            break
    if hata == 0 :
        sayi1 = float(sayi1)
        sayi2 = float(sayi2)
    else :
        print("Harf girmeyiniz   ")
        continue
    print(sayi1 / sayi2) '''

while True :
    try :
        ilk_sayi = float(input("ilk sayi gir : "))
        ikinci_sayi = float(input("ikinci sayi : "))
        print(ilk_sayi / ikinci_sayi)
    except ValueError :
        print("Lütfrn harf girmeyiniz .. ")
    except ZeroDivisionError :
        print("Herhangi bir sayının sıfıra bölümü tanımsızdır")