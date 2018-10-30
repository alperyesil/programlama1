from PyQt4.QtGui import*
from PyQt4.QtCore import*

class PDHHesapla(QDialog):

    def __init__(self,ebeveyn=None):
        super(PDHHesapla,self).__init__(ebeveyn)
        grid=QGridLayout()

        grid.addWidget(QLabel("Dönembaşı Personel Sayısı:"),0,0)
        self.dbps=QLineEdit()
        grid.addWidget(self.dbps,0,1)

        grid.addWidget(QLabel("Dönemsonu Personel Sayısı:"),1,0)
        self.dsps=QLineEdit()
        grid.addWidget(self.dsps,1,1)

        grid.addWidget(QLabel("İşten Çıkanların Toplam Sayısı:"),2,0)
        self.icts=QLineEdit()
        grid.addWidget(self.icts,2,1)

        grid.addWidget(QLabel("Personel Devir Hızı:"),3,0)
        self.pdh=QLabel("")
        grid.addWidget(self.pdh,3,1)

        hesaplabuton=QPushButton("Hesapla")
        grid.addWidget(hesaplabuton,4,0)
        self.connect(hesaplabuton, SIGNAL("pressed()"),self.PDHHesaplama)
        self.setLayout(grid)
        self.setWindowTitle("Personel Devir Hızı Hesaplama v1.0")
        self.resize(250,150)


    def PDHHesaplama(self):
        DBPerSay=int(self.dbps.text())
        DSPerSay=int(self.dsps.text())
        ICTopSay=int(self.icts.text())
        OPSay=(DBPerSay+DSPerSay)/2
        PDH=((ICTopSay+OPSay)/2)*100
        self.PDH.setText('<b>%0.lf</b>'%PDH)


app=QApplication([])
wdw=PDHHesapla()
wdw.show()
app.exec_()
