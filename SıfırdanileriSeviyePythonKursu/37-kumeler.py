A = set(("Merve", "Volkan", "Serhat", "Murat", "Begüm"))
B = set(("Merve", "Volkan", "Engin", "Altan", "Kenan", "Ceyda"))

yeniküme = A.difference(B) # A'nın B'den farkı
print(yeniküme)

print(B)
B.difference_update(A) # B'nin A'dan farkı olarak B kümesini güncelledi
print(B)


kesisim = B.intersection(A)
print(kesisim)