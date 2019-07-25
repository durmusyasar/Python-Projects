site1 = "http://google.com"
site2 = "http://gmail.com"

site1 = site1[0:7] + "www." + site1[7:]
site2 = site2[0:7] + "www." + site2[7:]

print(site1,site2, sep="\n") # sep parametresi ile aradaki ayırrma işelmini belirler
######
for i in reversed("merhaba"): # stringi ters çevirir
    print(i,end="") #aradaki boşluk bırakır
print("",sep="")
######
import locale # TÜRKÇE harfleri import etmemizi sağlar
locale.setlocale(locale.LC_ALL,"tr_TR.UTF-8")
print(sorted("çiçek",key=locale.strxfrm,reverse=True)) # sıralama yapar

#######
sesli_harfler = "aeıioöuü"
sessiz_harfler = "qwrtypğşlkjhgfdszxcvbnmç"
sesliler = ""
sessizler = ""

cumle = input("Cümleniz : ")
for harf in cumle :
    if harf in sesli_harfler:
        if harf not in sesliler:
            sesliler += harf
    elif harf in sessiz_harfler:
        if harf not in sessizler:
            sessizler += harf
    else :
        pass
print("Cümle karakter uzunluğu : ",len(cumle))
print("Cümledeki sesli harfler : ",sesliler)
print("Cümledeki sessiz harfler : ",sessizler)
