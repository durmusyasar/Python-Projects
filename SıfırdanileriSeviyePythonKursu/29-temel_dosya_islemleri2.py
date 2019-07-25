try:
    dosya = open("deneme.txt","w")
    print("Dosya var ")
except FileNotFoundError:
    print("Dosya yok")

with open("deneme.txt","a+") as dosya :
    dosya.write("Yazdım Çizdim")
    dosya.truncate(40)
    print(dosya.name)

if dosya.closed:
    print("Kapanmış")

