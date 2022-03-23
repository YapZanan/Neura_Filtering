from threading import *
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem, QDialog

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
