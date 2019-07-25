import sqlite3
con = sqlite3.connect("kutuphane.db") # Tabloya bağlanıyoruz
cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") # Sorguyu çalıştırıyoruz
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.

def veri_ekle():
    cursor.execute("insert into kitaplık Values ('İstanbul hatırası', 'Ahmet Ümit', 'Everest', 561)")
    con.commit()

def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
# isim = input("İsim:")
# yazar = input("Yazar:")
# yayınevi = input("Yayınevi:")
# sayfa_sayısı =  int(input("Sayfa Sayısı:"))

def veri_al():
    cursor.execute("Select * from kitaplık") # bütün bilgileri alıyoruz
    data = cursor.fetchall() # ver tabanındaki bilgileriçekmek için kullanıyoruz
    print("Kitaplık tablosunun bilgileri....\n\n")
    for i in data:
        print(i)
    # con.commit() işlemine gerek yok. Çünkü tabloda herhangi bir güncelleme yapmıyoruz.

def veri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık") # Sadece İsim ve Yazar özelliklerini alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri....")
    for i in data:
        print(i)

def veri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,)) # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)

def veri_guncelleme(eski_yayınevi, yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?", (yeni_yayınevi, eski_yayınevi))
    con.commit()

def veri_sil(yazar):
    cursor.execute("Delete  From kitaplık where Yazar = ?",(yazar,))
    con.commit()

# tablo_olustur() # bir defa çalıştır tablo oluştur

# veri_ekle() # içeriden veri ekleme

# deger_ekle(isim,yazar,yayınevi,sayfa_sayısı)# kullanıcıdan veri alma

# veri_al()
# print("--------------------------------------")
# veri_al2()
# print("--------------------------------------")
# veri_al3("1005")
# print("--------------------------------------")

# veri_guncelleme("1005", "KTU")
# veri_al()

# veri_sil("Ahmet Ümit")
veri_al()
con.close() # Bağlantıyı koparıyoruz

