meyve = "elma"

print(meyve.replace("e","E")) # harfi istenilene çevirme
#####
karakter_dizisi = input("gir : ")

kisaltma = ""

for kelime in karakter_dizisi.split():
    print(kelime)

######
karakter = "Trabzon Büyükşehir Belediyesi"
liste = karakter.split(sep=" ",maxsplit=1) # 1. kelimeden sonrasını alt satıra atar
liste2 = karakter.rsplit(sep=" ",maxsplit=1)# sağ taraftan itibaren 1. kelimeden sonrasını alt satıra atar
for i in liste:
    print(i)

for i in liste2:
    print(i)

#####

metin = """Kullanıcının gelir-gider hareketlerini kayıt altında tutabileceği 
ve bu hareketleri inceleyip planlayabileceği bir mobil uygulama hayal ediyoruz.
Gereksinim analizi maddelerimiz şu şekilde"""

print(metin.splitlines(keepends=True)) # string içindeki satır sonundaki kaçız karakterlerini gösterir
