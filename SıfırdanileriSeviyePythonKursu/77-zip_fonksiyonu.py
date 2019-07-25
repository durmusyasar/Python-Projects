 # nesne geriye döndürür ve iki listeyi demet haline getirir

liste1 = [1,3,5,7,9]
liste2 = [0,2,4,6,8]
liste3 = ['a','b','c','d','e']
a = list(zip(liste1,liste2))
print(a)
print("-------")
b = list(zip(liste1,liste2,liste3))
print(b)
print("-------")
for i,j in zip(liste1,liste3):
    print(i,j)
print("-------")
sözlük1 = {"Elma":1,"Armut":2,"Kiraz":3}
sözlük2 = {"Sıfır":0,"Bir":1,"İki":2}

c = list(zip(sözlük1,sözlük2))
print(c)
print("-------")
d = list(zip(sözlük1.values(), sözlük2.values()))