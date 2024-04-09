import datetime

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
        self.ui.pushButton_input.clicked.connect(self.new_services)

    def regist(self):
        FIO = self.ui.lineEdit_FIO.text()
        num = self.ui.lineEdit_num.text()
        email = self.ui.lineEdit_email.text()
        date = self.ui.lineEdit_date.text()
        self.APIBD.registration(FIO, num, email, date)

    def new_services(self):
        clientID = int(self.ui.lineEdit_clients.text())
        stat = str("На выполнении")
        date = str(datetime.date.today())
        info = self.ui.lineEdit_info.text()
        self.APIBD.new_service(clientID, info, date, stat)



















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Work()
    myapp.show()
    sys.exit(app.exec())
