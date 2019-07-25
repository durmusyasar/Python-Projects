liste = [1,2,3,4,5,6,7]
liste.append(34) # append metodu listenin en sonuna eleman eklememizi sağlar.
print(liste)

liste2 = [1,2,3,4,5,6,7]
liste2.extend([10,11,12])
print(liste2) # extend() metodu bir listeye başka bir listenin elemanları eklememizi sağlar.

liste3 = [1,2,3,4,5,6,7,8,9]
liste3.insert(2,"Python") # 2.indekse "Python" değerini ekliyoruz.
print(liste3)

liste4 = [1,2,3,4,5,6,7]
liste4.pop() # Son eleman siliniyor.
print(liste4)


liste5 = ["Python","Php","Java","C"]
liste5.remove("Python") # Python'ı siliyoruz.
print(liste5)


liste6 = [1,2,3,4,3,3,5,6,7,8,9]
print(liste6.index(3)) # 3 elemanı baştan başlayarak 2.indekste
print(liste6.index(3,3))


liste7 = [1,2,3,4,5,6,1,1,1,1,1,1,1,1,8]
print(liste7.count(1)) # verilen bir değerin listede kaç defa geçtiğini sayar.

liste8 = [12,-2,3,1,34,100]
liste8.sort()# metodu bir listenin elemanlarını sayıysa küçükten büyüğe , string ise alfabetik olarak sıralar
print(liste8)
liste9 = [12,-2,3,1,34,100]
liste9.sort(reverse = True)
print(liste9) # reverse = True değeri verilirse elemanları büyükten küçüğe sıralar.