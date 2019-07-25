metin1 = "qwertyuıopişljdsfdjbvncxgyfejkfhduısgıdfhguıdfhıog"
metin2 = "dıhfıuosdhuıfdsgyurfqwtweruıwqhrfudsgjfbhdsjkhjdsf"

harf_liste = ""

for harf in metin1 :
    if harf in metin2 :
        if harf not in harf_liste:
            harf_liste += harf
    else :
        pass # aksi durum yok ise

print(*harf_liste, sep=",")