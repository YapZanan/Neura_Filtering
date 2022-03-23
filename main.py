import os
from threading import *
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem, QDialog, QFileDialog


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.fname = None
        self.pushButton_Load.clicked.connect(self.loadfileketabel)


    def loadfileketabel(self):
        self.fname = QFileDialog.getExistingDirectory(self, 'Load File')
        if self.fname.isEmpty():
            print("wuhu")
        else:
            print(self.fname[0])
            print("aaa")

    def thread_load(self):
        t1 = Thread(target=self.loadfileketabel)
        t1.start()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
