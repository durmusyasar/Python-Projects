tr_karakter = "ışğçöü"
degisken = 0

kullanici_adi = input("Kullani Adi : ")

for harf in tr_karakter :
    if harf in kullanici_adi :
        print("Türkçe karakter kullanmayınız. ")
        break # şart sağlandığı gibi program sonlanur


if degisken == 0 :
    print("Kullanıcı kaydedildi")

else :
    print("Program durduruldu")