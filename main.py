import os
from threading import Thread
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QTableWidgetItem, QDialog, QFileDialog
import White_Balance

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.wb = White_Balance.White_Balance()

        self.path = None
        self.data = None
        self.image = QImage()

        self.pushButton_Load.clicked.connect(self.load_file_to_table)
        self.tableWidget_Tabel_File.clicked.connect(self.load_image_to_label)


    def wba(self):
        # aa = self.wb.retinex_adjust(self.get_selected_file_path())
        # self.image = QImage(aa, aa.shape[1], aa.shape[0], QImage.Format_RGB888)
        pass
    def select_folder(self):
        path = QFileDialog.getExistingDirectory(self, 'Load File')
        return path

    def get_selected_file_path(self):
        row = self.tableWidget_Tabel_File.currentRow()
        data = self.tableWidget_Tabel_File.item(row, 0)
        text = data.text()
        path_lengkap = self.path + "/" + str(text)
        return path_lengkap

    def load_file_to_table(self):
        self.path = self.select_folder()
        if self.path == '':
            print("No file selected")
        else:
            baca = os.listdir(self.path)
            self.data = []
            for file in baca:
                if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(
                        ".bmp") or file.endswith(".gif"):
                    self.data.append(file.replace(".jpeg", ""))
            total = len(self.data)
            self.tableWidget_Tabel_File.setRowCount(total)
            for i in range(total):
                self.tableWidget_Tabel_File.setItem(i, 0, QTableWidgetItem(str(self.data[i])))
            self.label_Camera.clear()

    def thread_load(self):
        t1 = Thread(target=self.load_file_to_table)
        t1.start()

    def load_image_to_label(self):
        path = self.get_selected_file_path()
        self.label_Camera.setPixmap(QPixmap(path))
        self.label_Camera.setScaledContents(True)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
