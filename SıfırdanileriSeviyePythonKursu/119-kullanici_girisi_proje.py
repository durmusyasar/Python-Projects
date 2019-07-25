import sys
from PyQt5 import QtWidgets
import sqlite3

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()
    
    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")

        self.cursor = baglanti.cursor()
        self.cursor.execute("Create Table if not exists üyeler (kullanıcı_adı TEXT, parola TEXT)")

        baglanti.commit()


    def init_ui(self):
        self.kullanıcı_adı = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani =QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanıcı_adı)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.show()

    def login(self):
        adi = self.kullanıcı_adı.text()
        par =self.parola.text()
 
        self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?",(adi,par))
        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen Tekrar Deneyiniz")
        else:
            self.yazi_alani.setText("Hoş Geldiniz " + adi )

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())