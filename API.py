import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Interface import Ui_MainWindow
from Orders import Ui_Order
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
        self.ui.pushButton.clicked.connect(self.check)

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

    def check(self):
        usersIDs = self.APIBD.show_all_service()
        print(len(usersIDs))
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget_2.setRowCount(len(usersIDs))
        self.ui.tableWidget_2.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        for i in range(len(usersIDs)):
            for j in range(5):
                if j < 4:
                    self.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(usersIDs[i][j])))
                else:
                    button = QtWidgets.QPushButton("Заказ")
                    button.setStyleSheet("background-color: white; border-radius: 10px;")
                    button.clicked.connect(self.openInterfaceOrders)
                    self.ui.tableWidget_2.setCellWidget(i, j, button)

    def openInterfaceOrders(self):
        self.other_interface = QtWidgets.QMainWindow()
        self.ui_other = Ui_Order()
        self.ui_other.setupUi(self.other_interface)
        self.other_interface.show()



















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Work()
    myapp.show()
    sys.exit(app.exec())
