oyum_tahtasi = [
    ["___", "___", "___"],
    ["___", "___", "___"],
    ["___", "___", "___"]
]
# koordinatlar
x_durumu = []
o_durumu = []

# kazanma ölçütleri
kazanma_olcutleri = [
    [[0,0], [0,1], [0,2]],
    [[1,0], [1,1], [1,2]],
    [[2,0], [2,1], [2,2]],
    [[0,0], [1,0], [2,0]],
    [[0,1], [1,1], [2,1]],
    [[0,2], [1,2], [2,2]],
    [[0,0], [1,1], [2,2]],
    [[0,2], [1,1], [2,0]]
]
kazanma_olcutleri.sort()
# Oyunun oynama kısmı x ya da 0 nun istenilen yere konulması
sira = 0 # oyun sırasını belirleme
while True: # sürekliliği sağlama
    sira += 1
    for i in oyum_tahtasi:
        print("\t".expandtabs(30),*i,end="\n\n ") # oyun tahtasını bastırma
    if sira % 2 == 0: # x oynuyacak
        isaret = "X".center(3) # merkeze yerleştir
    else :
        isaret = "O".center(3) # o oynuyacak merkeze yerleştir

    print("Oyun sırası: ",isaret)

    x = input("Soldan sağa doğru (1,2,3): ")
    # x'ten girilen değerin sayısal olması ve belirtilen aralıkta olması kontrolü
    try:
        x = int(x)
    except ValueError:
        print("Hatalı Girdiniz, Sıranızı kaybettiniz...")
        continue
    if x > 3 or x < 1:
        print("Hatalı Girdiniz, Sıranızı kaybettiniz...")
        continue

    y = input("Yukarıdan Aşağıya(1,2,3): ")
    # y'nin istenilen aralıkta ve sayısal olması isteniliyor
    try:
        y = int(y)
    except ValueError:
        print("Hatalı Girdiniz, Sıranızı kaybettiniz...")
        continue
    if y > 3 or y < 1:
        print("Hatalı Girdiniz, Sıranızı kaybettiniz...")
        continue

    x -= 1 # x'in konum sayısını azalt
    y -= 1 # y'nin konum sayısını azalt

    oyum_tahtasi[y][x] = isaret # elemanın koyulacak olduğu yer

    if sira % 2 ==0 :
        x_durumu += [[y,x]]
    else:
        o_durumu += [[y,x]]

    x_durumu.sort()
    o_durumu.sort()
    for i in kazanma_olcutleri:
        if x_durumu == i:
            for i in oyum_tahtasi:
                print("\t".expandtabs(30),*i,end="\n\n")
            print("Tebrikler 'X' kazandı...")
            quit(  )
        elif o_durumu == i:
            for i in oyum_tahtasi:
                print("\t".expandtabs(30),*i,end="\n\n")
            print("Tebrikler 'O' kazandı...")
            quit()