print("python".upper())
print("PYTHON".lower())
print("Herkes ana baba bacı gardaş".replace("a","o")) # çevirme
print("Python".startswith("py")) # başlangıçneyle başlıyor diye bakıyor
print("Python".startswith("Py"))
print("Python".endswith("on")) # sonu bitiyor mu
print("Python".endswith("an"))

# split(a) : Verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır.
liste = "Python Programlama Dili".split(" ") # Boşluk karakterine göre ayrıldı.
print(liste)

#strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.
a = "                   python                          ".strip() # değer göndermezsek varsayılan olarak boşluk karakteri
print(a)

# lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.
b = "                            python      ".lstrip()
print(b)


# rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.
c = "                            python      ".rstrip()
print(c)

# join() Listenin elemanlarını bir string değeriyle birleştirmemizi sağlar.
liste = ["21","02","2014"]
print("/".join(liste))

# count(x): Stringin içindeki x değerlerini sayar.
print("ada kapısı yandan çarklı".count("a"))

# count(x,index): Stringin içindeki x değerlerini verilen index değerinden başlayarak saymaya başlar.
print("ada kapısı yandan çarklı".count("a",2))

# find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
print("araba".find("a"))

# rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
print("araba".rfind("a"))
