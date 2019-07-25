def karelerial():
    sonuç = []
    
    for i in range(1,6):
        sonuç.append(i**2)
    return sonuç
 
 
print(karelerial())
print("############")


def karelerial():
    for i in range(1,6):
        yield i ** 2 # yield anahtar kelimesi generator'un değer üretmesi için kullanılıyor.
generator =  karelerial()

print(generator) # Generator objesi
iterator = iter(generator)
 
print(next(iterator)) # 1 değeri üretildi
print(next(iterator)) # 4 değeri üretildi 1 değeri tarihe karıştı.
print(next(iterator)) # 9 değeri üretildi 4 değeri tarihe karıştı.
print(next(iterator)) # 16 değeri üretildi 9 değeri tarihe karıştı
print(next(iterator)) # 25 değeri üretildi 16 değeri tarihe karıştı.
# print(next(iterator)) # Üretilecek değer kalmadı.

print("############")


liste = [i * 3 for i in range(5)]
 
print(liste)

generator = (i * 3 for i in range(5))
 
print(generator)
iterator2 = iter(generator)

print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print("############")


def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)
for i in carpimtablosu():
    print(i)

for i in range(100): # Sadece istediğimiz zaman sayılara ulaşıyoruz.
    print(i)