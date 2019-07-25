import os
from datetime import datetime

print(os.getcwd()) # Bulunduğun dizini söyler
# os.chdir("") Bulunduğun dizinin yerini değiştirir

# print(os.listdir()) # Dizindeki dosyaları listeler

for i in os.listdir():
    print(i)

# os.mkdir("Deneme") # Deneme adında bir dosya oluşturur
# os.rmdir("Deneme") # Deneme adında bir dosya siler
# os.removedirs("Deneme") # Deneme altındaki bütün dizinleri siler

# os.rename("deneme.txt", "deneme2.txt")

print(datetime.fromtimestamp(os.stat("kayit.txt").st_mtime))


# print(os.walk("home/durmus/Belgeler/durmusyasar/Python-my_studies"))
for i in os.walk("home/"):
    print(i)