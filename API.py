from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Interface import Ui_MainWindow
from General import DataBaseApi
import re

class Work(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.APIBD = DataBaseApi()

        self.ui.pushButton_reg.clicked.connect(self.regist)

    def regist(self):
        FIO = self.ui.lineEdit_FIO.text()
        num = self.ui.lineEdit_num.text()
        email = self.ui.lineEdit_email.text()
        date = self.ui.lineEdit_date.text()
        self.APIBD.registration(FIO, num, email, date)


















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Work()
    myapp.show()
    sys.exit(app.exec())
