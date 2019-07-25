liste = [1,2,3,3,1,1,2,2,2] # Aynı elemanı birçok defa  barındıran bir liste
x = set(liste) # Veri tipi dönüşümü
print(x) # Aynı elemanlar tek bir elemana indirgendi.

x = {"Python","Php","Java","C","Javascript"}
for i in x:
    print(i)


y = {1,2,3}
y.add(4) # Eleman Eklemek : add() metodu
print(y)

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
print(küme1.difference(küme2)) # İki kümenin farkı : difference() metodu
print(küme2.difference(küme1))
küme1.difference_update(küme2) # İki kümenin farkı ve güncelleme : difference_update() 

küme3 = {1,2,3,4,5,6}
küme3.discard(3) # Kümeden Eleman Çıkartmak : discard() metodu
print(küme3)

küme4 = {1,2,3,10,34,100,-2}
küme5 = {1,2,23,34,-1}
print(küme4.intersection(küme5)) # Küme kesişimleri : intersection() metodu
küme1.intersection_update(küme2) # Küme kesişimleri ve güncelleme : intersection_update() metodu

k1 = {1,2,3,10,34,100,-2}
k2 = {1,2,23,34,-1}
k3 = {30,40,50}
print(k1.isdisjoint(k2)) # Kümeler ayrık küme mi ? : isdisjoint() metodu
print(k1.isdisjoint(k3))


küm1 = {1,2,3}
küm2 = {1,2,3,4}
küm3 = {5,6,7}
print(küm1.issubset(küm2))
print(küm1.issubset(küm3)) # Alt kümesi mi ? : issubset() metodu

print(küm1.union(küm2)) # Birleşim Kümesi : union() metodu
küme2.update(küm3) # Birleşim Kümesi ve update : update() metodu
print(küm3)