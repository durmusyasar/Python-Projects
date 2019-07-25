'''
str.maketrans(),translate() >>örn:sözlük yapma
çeviri yaparak Türkçe karakterleri ingilizce karakterlere çevireceğiz
isalpha() >> karakter dizisinin alfabetik olup olmadığını denetleyeceğiz,
alfabedeki harflerden mi oluşuyor
isdigit() >> numaralardan mı oluşuyor
isalnum() >> hem harf hem numara ama özel karakterler olmaz
isdecimal >> saynın ondalık sistemde olup olmadığına bakar
isidentifier()  >> tanımlayıcı mı ?
isnumeric() >> numara mı?
isspace() >> boşluk mu?
isprintale() >> yazdırılabilir mi ?
'''

kaynak = "ıİüÜşŞöÖçÇğĞ"
hedef = "iIuUsSoOcCgG"

ceviri_tablosu = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde Türkçe karakterleri kullanamıyoruz"

print(metin.translate(ceviri_tablosu))

##############
metin2 = "asjdbjabfudahsfjd"
print(metin2.isalpha())
print(metin2.isdigit())

metin3 = "sdfds45sd4f5s4"
print(metin3.isalnum())

metin4 = "1234"
print(metin4.isdecimal())
print(metin4.isidentifier())
print(metin4.isnumeric())
print(metin.isspace())
print(metin3.isprintable())