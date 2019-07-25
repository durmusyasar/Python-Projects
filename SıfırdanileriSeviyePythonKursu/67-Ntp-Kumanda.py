import random
import time

class Kumanda():

    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["Trt"], kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal= kanal

    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Tv zaten açık")
        else:
            print("Tv Açılıyor....")
            self.tv_durum = "Açık"
    
    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Tv zaten kapalı")
        else:
            print("Tv kapanıyor...") 
            self.tv_durum = "Kapalı"
    
    def ses_ayararı(self):
        while True:
            cevap =input("sesi azalt: '<'\nSesi arttır: '>'\nÇıkış: q")
            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses: ",self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses: ",self.tv_ses)
            else:
                print("Ses güncellendi ",self.tv_ses)
                break
    
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor..")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)

    def rasgele_kanal(self):
        rasgele = random.randint(0, len(self.kanal_listesi)-1)
        # randint fonk verilen iki sayı arasında rasgele bir değer döndürür
        self.kanal = self.kanal_listesi[rasgele]
        print("Şuanki kanal: ",self.kanal)
    
    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv durumu: {}\nTv ses: {}\nKanal Listesi: {}\nŞuanki kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)
    
kumanda = Kumanda()
print("""

Televizyon Uygulaması

1 - Tv Aç

2 - Tv Kapat

3 - Ses Ayarları

4 - Kanal Ekle

5- Kanal Sayısını Öğrenme

6 - Rasgele Kanala Geçme

7 - Tv Bilgileri 

Çıkamk için "q" basın   
""")

while True:
    islem = input("İşlemi seçiniz...")

    if (islem == "q"):
        print("Program sonlandırılıyor...")
        break
    elif(islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"):
        kumanda.tv_kapat()
    elif(islem == "3"):
        kumanda.ses_ayararı()
    elif(islem == "4"):
        kanal_isimleri = input("Kanal isilerini ',' ile ayırarak giriniz.")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif(islem == "5"):
        print("Kanal sayısı: ",len(kumanda))
    elif(islem == "6"):
        kumanda.rasgele_kanal()
    elif(islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem...")