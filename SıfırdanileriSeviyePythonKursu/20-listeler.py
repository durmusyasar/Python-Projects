listemiz = ["ince Mhemet", "python", "C++",1 ,2, 3,4, 5, ["Merhaba", "Python"]]

print(listemiz[1])
print(listemiz[-1])
print(listemiz[-1][1])

#############

veri =input("Gir : ")
liste = list(veri)
print(liste)

#############

listem = ["Durmuş",1,2,3,4,["merhaba", "dünya"]]

print(listem)

listem[5][1] = "Python"

print((listem))

del listem[4]

print(listem)

ad = listem.index("Durmuş") # kaçıncı indiste olduğunu bulma
print(ad)

#####################

listem += ["deneme"]
print(listem)

listem[0:3] = 5,6,7

print(liste[::-1])