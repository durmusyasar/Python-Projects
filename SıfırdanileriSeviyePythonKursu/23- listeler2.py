liste = [1,2,3,4,5,6]
print(liste)

liste.append(7) # listeye eleman ekleme
print(liste)

liste.pop(3) # listeden eleman çıkarma
print(liste)

liste.sort() # listeyi sıralama
print(liste)

liste.sort(reverse=True) # tersten sıralama
print(liste)

liste.insert(2,8) # listenin neresine eleman ekleyeceğimizi belirtme
print(liste)

liste.remove(8) # listeden eleman silme
print(liste)

liste.reverse() # listeyi ters çevirme
print(liste)

a = liste.index(3)# öğenin sıra numarası
print(a)

b = liste.count(2) # öğeninn tekrar sayısı
print(b)

c = liste.copy() # listeyi kopyalama
print(c)

d = liste.clear()
print(d)