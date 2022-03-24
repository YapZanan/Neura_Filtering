import os
from threading import *
from PyQt5 import QtWidgets, uic, QtGui
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem, QDialog, QFileDialog
import White_Balance

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.wb = White_Balance.White_Balance()

        self.path = None
        self.data = None
        self.image = QImage()

        self.pushButton_Load.clicked.connect(self.loadfileketabel)


        # self.tableWidget_Tabel_File.clicked.connect(self.loadkelabel)

        self.tableWidget_Tabel_File.clicked.connect(self.wba)
        # self.checkBox_Vignette.stateChanged.connect(self.wba)



    def wba(self):
        self.wb.grayworld(self.loadkelabel(), len(self.data))
        # print("aaa")

    def bacafolder(self):
        #, options= QFileDialog.DontUseNativeDialog
        path = QFileDialog.getExistingDirectory(self, 'Load File')
        return path


    def loadkelabel(self):
        row = self.tableWidget_Tabel_File.currentRow()
        data = self.tableWidget_Tabel_File.item(row, 0)
        text = data.text()
        path_lengkap = self.path + "/" + str(text)
        # print(self.path_lengkap)
        return path_lengkap
        # self.label_Camera.setPixmap(QtGui.QPixmap(path))
        # self.label_Camera.setScaledContents(True)


    def loadfileketabel(self):
        self.path = self.bacafolder()
        if self.path == '':
            print("Tidak memilih file")
        else:
            baca = os.listdir(self.path)
            self.data = [s.replace(".jpeg", "") for s in baca]
            total = len(self.data)
            self.tableWidget_Tabel_File.setRowCount(total)
            for i in range(total):
                self.tableWidget_Tabel_File.setItem(i, 0, QTableWidgetItem(str(self.data[i])))
                # self.Tabel_Mahasiswa.setItem(i, 1, QTableWidgetItem(str(password[i])))



    def thread_load(self):
        t1 = Thread(target=self.loadfileketabel)
        t1.start()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
