'''
rjust() ve ljust() >> sağa yaslama ve sola yaslama (hizalama)
zfill() >> karakter dizisinin sol tarafına istedimiz sayıda sıfır ekleriz
partition() ve rpartition() >> karakter dizisini belli ölçütte bölme
encode() >> python3 te kullanılan karakter kodlaması default = utf-8
expandtabs() >> bir karakter dizisi içerisindeki sekme boşluklarını genişletme
'''

ad = "Durmuş"
soyad = "YAŞAR"

print("Adı".ljust(10),":",ad)
print("Soyad".ljust(10),":",soyad)

print("Adı".rjust(10,"."),":",ad)
print("Soyad".rjust(10,"."),":",soyad)

##############
a = "12"
print(a.zfill(5))

for i in range(11):
    print(str(i).zfill(2))

###########
kardiz = "istanbul"
kardiz2 ="adana"
print(kardiz.partition("an"))
print(kardiz2.rpartition("a"))

#######
print("çiçek".encode("cp1254"))

########
print("merhaba\tDurmuş".expandtabs(20))