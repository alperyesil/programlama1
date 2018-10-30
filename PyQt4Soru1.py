from PyQt4.QtGui import*
from PyQt4.QtCore import*

class tablo1(QDialog):

    def __init__(self,ebeveyn=None):
        super(tablo1, self).__init__(ebeveyn)
        self.initUI()

    def initUI(self):
        self.setGeometry(600,300,400,200)
        self.setWindowTitle('Kişi Bilgileri')
        grid=QGridLayout()
        self.setLayout(grid)
        veriler={'Adı':['Can','Semih','Büşra'],'Soyadı':['Aydın','Yarar','Demirgüreşçi'],'Bölüm':['YBS','YBS','İktisat']}

        table=QTableWidget(self)
        table.setRowCount(3)
        table.setColumnCount(3)

        liste=[]
        for a, key in enumerate(sorted(veriler.keys())):
            liste.append(key)
            for b, item in enumerate(veriler[key]):
                yitem=QTableWidgetItem(item)
                table.setItem(a,b,yitem)
        table.setHorizontalHeaderLabels(liste)
        grid.addWidget(table,0,0)
        self.show()

app=QApplication([])
wdw=tablo1()
wdw.show()
app.exec_()
