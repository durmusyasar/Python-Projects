girdi = input("Gir : ")

alfabe = "abcçdefgğhıijklmnoöprsştuüvyzwqx"

for harf in alfabe :
    if girdi.endswith(harf): # stringin son harfini döndürür
        print("Harf bulundu", harf)
    else :
        pass
##########
for harf in alfabe :
    if girdi.startswith(harf): # stringin ilk harfini döndürür
        print("Harf bulundu", harf)
    else :
        pass
##########
kardiz = "python programlama dilleri"
print(kardiz.capitalize()) # stringin ilk harfini büyük yazar
print(kardiz.title())  # stringin kelimelerininin ilk harfini büyük yapar
print(kardiz.swapcase()) # büyük harfi küçük küçük harfi büyük yapar
#############

kardiz2 = "istihza"
print(kardiz2)
print(kardiz2.strip("ai")) # baştan ya da sondan eleman silme
print(kardiz2.rstrip("ai")) # sağdan eleman silme
print(kardiz2.lstrip("ia")) # soldan eleman silme