# all fonk. bütün değerler True , enaz bir değer False ise False sonuç döndürür
# any fonk.  bütün değerler False ise False, en az bir değer True ise True sonuç döndürür.

liste = [True,False,True,False,True]
a = all(liste)
print(a)

liste2 = [1,2,3,4,5]
b = all(liste2)
print(b)

print("---------")
c = any(liste)
d = any(liste2)
print(c)
print(d)