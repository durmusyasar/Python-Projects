isim = "Durmuş"
soyad = "YAŞAR"
print("Merhaba {} {}".format(isim, soyad))
print("Merhaba {0} {1}".format(isim, soyad))
print("Merhaba {:<10} {}".format(isim, soyad))
print("Merhaba {:>10} {}".format(isim, soyad))

sayi = input("Ondalık tabandaki sayi = ")

try:
    sayi = int(sayi)
except ValueError:
    print("Yalnızca sayi giriniz ")
    quit()

print("Sonuç : {:X}".format(sayi))
print("Sonuç : {:b}".format(sayi))