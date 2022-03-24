import os
from threading import *
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem, QDialog, QFileDialog


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)

        self.path = None
        self.data = None


        self.pushButton_Load.clicked.connect(self.loadfileketabel)


    def bacafolder(self):
        #, options= QFileDialog.DontUseNativeDialog
        path = QFileDialog.getExistingDirectory(self, 'Load File')
        return path

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
