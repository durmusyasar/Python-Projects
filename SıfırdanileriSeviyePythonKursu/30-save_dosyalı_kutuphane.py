liste = []

with open("kayit2.txt","a") as startFile:
    pass

with open("kayit2.txt") as readFile:
    for i in readFile.readlines():
        liste.append(i)

menu = """
[1] Kitap Ekle
[2] Kitap Çıkar
[3] Kitap Listele
[Q] Kaydet ve Çık

"""

while True:
    print(menu)
    giris = input("Seçiniz : ")

    if giris == "1":
        ad = input("Eklenecek kitap adı : ")
        liste.append(ad+"  \n")
        print("Kitap Eklendi!")
        print("==============")

    elif giris == "1":
        ad = input("Çıkartılacak kitap adı : ")
        liste.remove(ad+"\n")
        print("Kitap Çıkartıldı!")
        print("==============")

    elif giris == "3":
        for i in liste:
            print(i,end="")

    elif giris == "q" or giris == "Q":
        with open("kayit2.txt","w") as writeFile:
            for i in liste:
                writeFile.write(i)