class Calisan():
    def __init__(self, isim, maas, departman):
        print("Çalışan fonksiyonun init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgiler(self):
        print("Çalışan sınıfının bilgileri")
        print("isim : {}\nmaaş: {}\ndepertman:{}".format(self.isim, self.maas, self.departman))

    def depertman_degistir(self, yeni_depertman):
        self.departman = yeni_depertman

class Yonetici(Calisan):
    # override etme kisi_sayisi ek özellik olduğu için yeniden tanımlanmalı fonk
    def __init__(self, isim, maas, departman, kisi_sayisi):
        print("Yönetici fonksiyonun init fonksiyonu")
        # super anahtar kelimesini(Kalıtım ile berarber) kullandığımızdan dolayı bu 3 satırı siliyoruz 
        super().__init__(isim, maas , departman)
        # self.isim = isim
        # self.maas = maas
        # self.departman = departman
        self.kisi_sayisi = kisi_sayisi

    def bilgiler(self):
        print("Çalışan sınıfının bilgileri")
        print("isim : {}\nmaaş: {}\ndepertman:{}\nsorumlu kişi sayısı :{}".format(
            self.isim, self.maas, self.departman, self.kisi_sayisi))

    def zam_yap(self, zam_miktarı):
        self.maas += zam_miktarı

# yonetici = Yonetici("Durmuş YAŞAR", 400, "Bilişim")
# print(yonetici.bilgiler())

# yonetici.depertman_degistir("Yazılımcı")
# print(yonetici.bilgiler())

# yonetici.zam_yap(500)

# override dan ve super anahtar kelimesinden sonra 
yonetici = Yonetici("Durmuş YAŞAR", 400, "Bilişim", 400)
print(yonetici.bilgiler())