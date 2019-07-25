ikiylecarp = lambda x : x * 2
print(ikiylecarp(3))

toplama = lambda  x, y, z :x + y + z
print(toplama(1,4,5))

terscevir = lambda  s : s[::-1]
print(terscevir("durmus"))

#def cifttek(sayi):
#    return sayi % 2 == 0

cifttek = lambda sayi : sayi % 2 == 0
print(cifttek(13))
print(cifttek(14))