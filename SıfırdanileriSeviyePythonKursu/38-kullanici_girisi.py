print("""************************
Kullanıcı Girişi
************************
""")

sys_kullanici_adi = "Durmuş"
sys_parola = "12345"
giris_hakkı = 3

kullanici_adi = input("Kullanıcı Adı : ")
parola = input("Parola : ")
while True:
    if (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatalı...")
        giris_hakkı - = 1

    elif (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı Adı Hatalı ....")
        giris_hakkı - = 1

    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giris_hakkı - = 1

    else:
        print("Sisteme Başarıyla Giriş Yapıldı ... ")
        break

    if (giris_hakkı == 0):
        print("Giriş Hakkınız Bitti....")
        break