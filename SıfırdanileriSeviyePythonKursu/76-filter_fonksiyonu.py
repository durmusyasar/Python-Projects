# reduce(fonksiyon , iterasyon yapılacak veri tipi)
# fonksiyon True ya da False döndürmeli reduce fonk ile aynı mantıktadır.
# obje geri döndürür

a = filter(lambda x: x%2==0 , [1,2,3,4,5,6,7,8,9])
print(list(a))

def asalmı(x):
    i = 2
    if (x == 1):
        return False 
    elif(x == 2):
        return True
    else:
        while(i < x):
            if (x % i == 0):
                return False 
            i += 1
    return True

b = filter(asalmı, range(1,100))
print(list(b))