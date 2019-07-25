# her bir elemanı indeksleyerek bir nesne döndürür

liste = ["Elma","Armut","Muz","Kiraz"]
a = list(enumerate(liste))
print(a)
print("------------")

for i,j in enumerate(liste):
    print(i,j)