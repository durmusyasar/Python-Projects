karakterler = {

    "Ninja" : {

        "Sağlık" : 100,
        "Güç"    : 16,
        "Silah"  : "Bıçak"
    },

    "Savaşçı" : {

        "Sağlık" : 100,
        "Güç"    : 20,
        "Silah"  : "Kılıç"
    }
}

karakter1 = karakterler["Savaşçı"]
karakter2 = karakterler["Ninja"]

print("Karakterlerin sağlık değeri : ", karakter1["Sağlık"])
print("Karakterlerin güç değeri : ", karakter1["Güç"])
print("Karakterin silahı : ", karakter1["Silah"])

karakter2["Sağlık"] = karakter2["Sağlık"] - karakter1["Güç"]
+
print("Karakter2'nin Şuanki Sağlığı : ",karakter2["Sağlık"])