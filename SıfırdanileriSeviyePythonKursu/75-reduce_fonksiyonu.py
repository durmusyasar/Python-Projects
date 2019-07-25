# reduce(fonksiyon , iterasyon yapılacak veri tipi)
# fonk. alına veri tipinin (liste) soldan ilk iki elemanına uygular oradan alınan değeri 3 bu şekilde devam eder

from functools import reduce

def toplama(x,y):
    return x + y

a = reduce(toplama, [12, 20, 35, 48])
print(a)

b = reduce(lambda x,y : x*y, [12, 20, 35, 48])
print(b)

def maksimum(x,y):
    if(x > y):
        return x
    else:
        return y

c = reduce(maksimum, [12, 20, 35, 48])
print(c)