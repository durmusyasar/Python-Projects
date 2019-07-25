kutuphane = ["Python","C++", "Ruby"]
secenekler = """
[1] Kitapları Listele
[2] Kitap Ekle
[3] Kitap Sil
[4] Kitap Ara
[Q] Çıkış
"""

while True:
    print(secenekler)
    islem = input("İşleminiz: ")
    if islem == "1":
        for sayi, kitap in enumerate(kutuphane):
            print(sayi+1,kitap)

    elif islem == "2":
        k_adi = input("Kitap Adı : ")
        kutuphane += [k_adi]
        print("Kitap Eklendi....")
        input("Devam Etmek için 'Enter'a basın")
    elif islem == "3":
        durum = False
        k_adi = input("Kitap Adı : ")
        for kitap in kutuphane:
            if k_adi == kitap:
                durum = True
                break
        if durum == True :
            oge_numarasi = kutuphane.index(k_adi)
            del kutuphane[oge_numarasi]
            print("Kitap Silindi....")
        else:
            print("Kitap mevcut Değil")
            input("Devam Etmek için 'Enter'a basın")
    elif islem == "4":
        durum = False
        k_adi = input("Kitap Adı : ")
        for kitap in kutuphane:
            durum = True
            break
        if durum :
            print("Kitap Kütüphanede Mevcut")
        else :
            print("Kitap Mevcur Değil")
    elif islem == "Q" or islem == "q":
        break
    else:
        print("Hatalı Giriş Yapıldı...")