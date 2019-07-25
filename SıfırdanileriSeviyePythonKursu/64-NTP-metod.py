class Yazilimci():

    def __init__(self, isim, soyisim, numara, maas, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller

    def bilgiler(self):
        print("""
        Yazilimci objesinin özelillikleri 
        isim : {}
        soyisim : {}
        numara : {}
        maas : {}
        Bildiği Diller : {}

        """.format(self.isim , self.soyisim, self.numara, self.maas, self.diller))

    def zam_yap(self, zam_miktarı):
        print("Zam yapılıyor ...")
        self.maas+=zam_miktarı

    def dil_ekle(self,yeni_dil):
        print ("Dil ekleniyor...")
        self.diller.append(yeni_dil)

yazilimci = Yazilimci("Dumuş", "YAŞAR", 314040, 400, ["Python", "C", "C++"])

print(yazilimci.bilgiler())
