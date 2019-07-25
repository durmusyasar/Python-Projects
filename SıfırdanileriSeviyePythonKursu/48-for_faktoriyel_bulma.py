print(".....Faktöriyel Bulma .....")

print("Çıkmak için q'a basın")

while True:
    sayi = input("Sayi : ")
    if(sayi == "q"):
        print("Program Sonlandırılıyor....")
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1

        for i in range(2, sayi+1):
            print("Faktöriyel",faktoriyel,"i : ",i)
            faktoriyel *= i
        print("Faktöriyel : ", faktoriyel)