izinli_karakterler = "0123456789"

tc = input("gir : ")

if len(tc) != 1 :  # string uzunluğunu döndürür
    print("Hatalı")

else :
    if tc in izinli_karakterler :
        print("Doğru")
    else :
        print("Harf ya da simgeler kullanılamaz")