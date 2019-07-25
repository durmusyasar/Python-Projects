import sys
from PyQt5 import QtWidgets, QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv) # uygulama oluştur
    pencere =QtWidgets.QWidget() # Pencere oluştur
    pencere.setWindowTitle("PyQt5 Dersleri 1") # pencere Adı
    etiket1 = QtWidgets.QLabel(pencere) # Pencere içine yazı ekleme
    etiket1.setText("Burası Bir yazıdır")
    etiket1.move(200,30) # yazının  konumunu belirleme
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("python.png")) # resim ekleme
    etiket2.move(70.100)
    buton =QtWidgets.QPushButton(pencere) # buton oluşturma
    buton.setText("Burası Bir butondur...")
    buton.move(190,80) 




    pencere.setGeometry(100,100,500,500)# Masaüstünde Uygulama Hangi konumdan başlayacak ve boyutu 
    pencere.show() # Pencereyi göster

    sys.exit(app.exec_()) # Pencere sürekli açık kalsın diye döngü
    