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

    def regist(self):               #Добавление клиента В БД
        FIO = self.ui.lineEdit_FIO.text()
        num = self.ui.lineEdit_num.text()
        email = self.ui.lineEdit_email.text()
        date = self.ui.lineEdit_date.text()
        self.APIBD.registration(FIO, num, email, date)

    def new_services(self):             #Добавление заказа в БД
        clientID = int(self.ui.lineEdit_clients.text())
        stat = str("На выполнении")
        date = str(datetime.date.today())
        info = self.ui.lineEdit_info.text()
        summ = int(self.ui.lineEdit_sum.text())
        self.APIBD.new_service(clientID, info, date, stat, summ)

    def check(self):            #Внесение в таблицу информации с БД
        usersIDs = self.APIBD.show_all_service()
        print(len(usersIDs))
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget_2.setRowCount(len(usersIDs))
        self.ui.tableWidget_2.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        for i in range(len(usersIDs)):
            for j in range(5):
                if j == 0:
                    save = str(usersIDs[i][j])
                    print(save)
                if j < 4:
                    self.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(usersIDs[i][j])))
                else:
                    prints = "Заказ №" + save
                    button = QtWidgets.QPushButton(prints)
                    button.setStyleSheet("background-color: white; border-radius: 10px;")
                    button.clicked.connect(lambda _, row=save: self.openInterfaceOrders(row))
                    self.ui.tableWidget_2.setCellWidget(i, j, button)

    def openInterfaceOrders(self, row):             #Открытие окна заказа
        self.other_interface = QtWidgets.QMainWindow()
        self.ui_other = Ui_Order()
        self.ui_other.setupUi(self.other_interface)
        self.other_interface.show()

        self.ui_other.TextOrder_id.setText("Заказ № " + row)
        InfoID = self.APIBD.showOrderDialog(row)

        html_text = "<div align='center'>Заказ № " + row + "</div>"
        self.ui_other.TextOrder_id.setText(html_text)

        html_text = "<div align='center'>Клиент:</div><div align='center'>" + str(InfoID[0][0]) + "</div>"
        self.ui_other.textBrowser_FIO.setText(html_text)

        html_text = "<div align='center'>Дата:</div><div align='center'>" + str(InfoID[0][1]) + "</div>"
        self.ui_other.textBrowser_date.setText(html_text)

        self.ui_other.textBrowser_info.setText(str(InfoID[0][2]))

        html_text = "<div align='center'>Стоимость:</div><div align='center'>" + str(InfoID[0][3]) + "</div>"
        self.ui_other.textBrowser_sum.setText(html_text)

        #Доп. настройка стилей
        style = ("font: 87 12pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui_other.textBrowser_FIO.setStyleSheet(style)
        self.ui_other.TextOrder_id.setStyleSheet(style + "font: 87 22pt \"Segoe UI Black\";")
        self.ui_other.textBrowser_date.setStyleSheet(style)
        self.ui_other.textBrowser_info.setStyleSheet(style)
        self.ui_other.textBrowser_sum.setStyleSheet(style)
















if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Work()
    myapp.show()
    sys.exit(app.exec())
