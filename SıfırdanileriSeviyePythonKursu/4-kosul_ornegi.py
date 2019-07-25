kullanici1 = "Durmuş"
kullanici2 = "Emin"
kullanici3 = "Yusuf"

giris = input("Kullanıcı Adınız : ")

if (giris == kullanici1):
    print("Hoşgeldiniz {}".format(kullanici1))

elif (giris == kullanici2):
    print("Hoşgeldiniz {}".format(kullanici2))

elif (giris == kullanici3):
    print("Hoşgeldiniz {}".format(kullanici3))

else :
    print("Böyle bir kullanıcı mevcut değil")