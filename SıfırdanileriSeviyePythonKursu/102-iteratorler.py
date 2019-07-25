liste = [1,2,3,4,5,6,7,8]
iterator = iter(liste)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print("####################")

for i in liste:
    print(i)

# bunun python'daki eşdeğeri arka pşanda çalışan

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi # Kanal Listemiz
        self.index = -1 # İndeksimiz
        
    def __iter__(self):
        return self # iterator oluşturduğumuzda (iter fonksiyonu çağrıldığında )objemizi döneceğiz.
    def __next__(self): # next fonksiyonu çağrıldığında burası çalışacak.
        self.index += 1
        if (self.index < len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration

kumanda = Kumanda(["Kanal d","Trt","Atv","Fox","Bloomberg"]) # Objemizi oluşturuyoruz.

iterator =  iter(kumanda) # Objemiz iterable olduğu için iterator oluşturulabilir.

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))