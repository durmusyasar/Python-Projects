def ekstra(fonk):
    def wrapper(sayilar):
        ciftler_toplamı = 0
        cift_sayilar = 0
        tekler_toplamı = 0
        tek_sayilar = 0

        for sayi in sayilar:
            if(sayi%2 == 0):
                ciftler_toplamı += sayi
                cift_sayilar += 1
            else:
                tekler_toplamı += sayi
                tek_sayilar += 1
    
        print("Teklerin ortalaması : ", tekler_toplamı/tek_sayilar)
        print("Çiftlerin ortalaması : ", ciftler_toplamı/cift_sayilar)
        fonk(sayilar)
    return wrapper

@ekstra
def ortalama_bul(sayilar):
    toplam = 0

    for sayi in sayilar:
        toplam += sayi
    
    print("Genel Oratalama :", toplam/len(sayilar))


print(ortalama_bul([1,2,3,4,5,6,4,8,4,4,1,4,41]))
