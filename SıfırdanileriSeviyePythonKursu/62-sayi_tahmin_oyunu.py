import random
import time

print("""
**********************************

Sayi Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin et

**********************************
""")

rasgele_sayi = random.randint(1, 40)
tahmin_hakkı = 7

while True:
    tahmin = int(input("Tahmininiz : "))

    if (tahmin < rasgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayi söyleyiniz...")
        tahmin_hakkı -= 1

    elif (tahmin > rasgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayi söyleyiniz...")
        tahmin_hakkı -= 1

    else:
        print("Bilgiler sorgulanıyor")
        time.sleep(1)
        print("Tebrikler! Sayımız : ",rasgele_sayi)
        break
    if (tahmin_hakkı == 0):
        print("Tahmin hakkınız bitti...")
        print("Sayımız : ",rasgele_sayi)
        break