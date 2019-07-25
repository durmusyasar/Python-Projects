class Araba():

    model = "Renault"
    renk = "Beyaz"
    beygir = 90
    silindir = 3

    def __init__(self, model, renk, beygir, silindir):
        # her bir obje için farklı veri üretmemizi sağlayan method
        print("init fonksiyonu çağrıldı")
        self.model = model
        self.renk = renk
        self.beygir = beygir
        self.silindir = silindir

araba1 = Araba("BMW","Siyah",110,4)
print(araba1.model)