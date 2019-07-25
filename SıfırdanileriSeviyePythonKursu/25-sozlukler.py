sozluk = {"bir":1,"iki":2}

print(sozluk["iki"])

sozluk["üc"] = 3

print(sozluk)

sozluk["bir"] = 6

print(sozluk )
#####################

a = {"bir": [1,2,3,4], "iki": [[1,2],[3,4],[5,6]], "üç": 15}

print(a["iki"])

print(a["iki"][1])

print(a["iki"][1][1])


##################  iç içe sözlük

b = {"sayilar":{"bir": 1, "iki": 2, "üç": 3},"meyveler":{"kiraz": "yaz", "portakal": "kış", "erik": "yaz"}}

print(b["sayilar"])
print(b["sayilar"]["iki"])

#################     Metotlar

print(sozluk.keys())
print(sozluk.values())
print(a.items())