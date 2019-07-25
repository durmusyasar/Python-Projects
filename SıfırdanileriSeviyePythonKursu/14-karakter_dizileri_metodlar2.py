isim1 = "Durmuş"
isim2 = "Yusuf"

ara = input("Aranacak isim : ")

if ara == isim1 :
    print("Kullanıcı veri tabanında mevcut ! ")
if ara.lower() == isim2.lower(): # büyük küçük harf uyumluluığu
    print("Kullanıcı veri tabanında mevcut ! ")
else :
    print("kullanıcı veri tabanında mevcut değil !!! ")

########

text = "ADIYAMAN"
text = text.replace("I","ı").replace("İ","i") # burada ı yı küçültürken i ye çeviriyor bunu önlemek için
print(text.lower())
print(text.islower()) # string teki harflerin küçük mü kontrolü


######
text2 ="adana"
print(text2.upper ()) # stringi büyük harfe çevirir
print(text2.isupper())# büyük mü

############

