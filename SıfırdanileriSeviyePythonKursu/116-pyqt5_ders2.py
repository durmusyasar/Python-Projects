import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    okey = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    # # butonların ekranın boyutunu değiştirdikçe değişmemesini sağlamak için
    # h_box = QtWidgets.QHBoxLayout()

    # # burada h_box.addStretch() kullanırsak sağa yaslı olur butonlar
    # h_box.addWidget(okey)
    # # burada h_box.addStretch() tanımlanırsa okey sola iptal sağa yaslı olur 
    # h_box.addWidget(cancel)

    # # butonları ekledikten sonra sağ tarafı boş bırakalım (sol tarafa yaslı)
    # h_box.addStretch()

    # ######
    # okey2 = QtWidgets.QPushButton("Tamam2")
    # cancel2 = QtWidgets.QPushButton("İptal2")
    # v_box = QtWidgets.QVBoxLayout()
    # v_box.addWidget(okey2)
    # v_box(cancel2)
    # v_box.addStretch()


    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okey)
    h_box.addWidget(cancel)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)
    



    pencere = QtWidgets.QTabWidget()
    pencere.setWindowTitle("PyQt5 Derseri 2")
    # # Horizonal Layout box ları belirtiyoruz 
    pencere.setLayout(h_box)
    # pencere.setLayout(v_box)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())