import sys

# a = int(input("a: "))
# b = int(input("b: "))
# sys.exit()
# c = int(input("c: "))


sys.stderr.write("Bu bir hata mesajı ...\n")
sys.stderr.flush() # buffer'ı hemen yaz
sys.stdout.write("Bu normal çıktıdır\n")


print(sys.argv)


for i in sys.argv:
    print(i)

def kok_bul(a,b,c):
    delta = b ** 2 - 4 * a * c
    if(delta < 0):
        print("Reel kök yok")
    else:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        return (x1,x2)

if len(sys.argv) == 4:
    print("Kök Bulma", kok_bul(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[2])))
else:
    sys.stderr.write("Lütfen Doğru değer giriniz")
    sys.stderr.flush()