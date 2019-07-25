class Kitap():
    # pass
    def __init__(self, isim, yazar, sayfa_sayısı, tur):
        print("Kendi oluşturduğum __init__ metodu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tur = tur

    def __str__(self):
        print("Kendi oluşturduğum __str_ metodu")
        return "isim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür:{}".format(self.isim , self.yazar, self.sayfa_sayısı, self.tur)

    def __len__(self):
        print("Kendi oluşturduğum __len__ metodu")
        return self.sayfa_sayısı
    
    def __del__(self):
        print("Kendi oluşturduğum __del__ metodu")
        print("Kitap objesi siliniyor..")


kitap = Kitap("İstanbul hatırası", "Ahmet ÜMİT", 561, "Polisiye")

print(kitap)
print(len(kitap))
del kitap
# kitap = Kitap()  # __init__ metodu

# print(kitap)# __str__ metodu
# len(kitap)# __len__ metodu
# del kitap # __ del __ metodu