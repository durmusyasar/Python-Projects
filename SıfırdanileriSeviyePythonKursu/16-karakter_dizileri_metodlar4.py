'''
join() >> öğeleri birleştirir
count() >> karakterlerin tekrar sayısı
index() ve rindex >> öğenin sıra numarası ===== Value Error !
find ve rfind >> öğenin sıra numarası ==== -1
center >> karakter dizisi merkezleme
'''

kardiz = "python programlama dili"

veriler = kardiz.split()
print("-".join(veriler))
print(kardiz.count("a"))

print(kardiz.index("d")) # ilk karşılaştığını vericek
print(kardiz.rindex("a")) # karakter yok value Error

print(kardiz.find(("n")))
print(kardiz.rfind("z")) # karakter yok -1

print(kardiz.center(8))