print("""

#####################
#                   #
#  Hesap Makinesi   #
#                   #
#####################

+ -->> Toplama
- -->> Çıkarma
* -->> Çarpma
/ -->> Bölme
** -->> Üs Alma

""")

islem = input("İsleminizi belirtin : ")

sonuc = eval(islem) # print gibi bir fonksiyondur

print("Sonuç: ",sonuc)