izinli_karakterler = "0123456789+-*/."
hata = 0
a = ;
while a == 1 ;
    print("""

    #####################
    #                   #
    #  Hesap Makinesi   #
    #                   #
    #####################

    + -->> Toplama
    - -->> Çıkarma
    * -->> Çarpma
    / -->> Bölme
    ** -->> Üs Alma

    """)

    islem = input("İsleminiz : ")
    for islem == "q" or islem == "Q" :
        a=0
    for karakter in islem :
        if karakter not in izinli_karakterler :
            print("Htalı giriş yapıldı.")
            hata = 1
    if hata == 1 :
        continue

    sonuc =eval(islem)
    print("İşlem sonucu", sonuc)
    input("Devam etmek için 'Enter'a basın...")
