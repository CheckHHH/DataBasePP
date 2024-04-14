import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
from General import DataBaseApi

import re

#Интерфейсы
from interface.Interface import Ui_MainWindow
from interface.Orders import Ui_Order
from interface.Clients import Ui_ClientDialog


class Work(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer()

        self.APIBD = DataBaseApi()

        self.ui.pushButton_reg.clicked.connect(self.regist)
        self.ui.pushButton_input.clicked.connect(self.new_services)
        self.ui.pushButton.clicked.connect(self.checkOrders)
        self.ui.pushButton_2.clicked.connect(self.checkClients)
        self.checkOrders()
        self.checkClients()

    def regist(self):               #Добавление клиента В БД
        FIO = str(self.ui.lineEdit_FIO.text())
        num = str(self.ui.lineEdit_num.text())
        email = str(self.ui.lineEdit_email.text())
        date = str(self.ui.lineEdit_date.text())
        if FIO == "" or num == "" or email == "" or date == "":
            string = "Ошибка"
        else:
            self.APIBD.registration(FIO, num, email, date)
            string = "Успешно"
        html_text = "<div align='center'>" + string + "</div>"
        self.ui.textBrowser_errNewClient.setText(html_text)
        style = ("font: 87 10pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui.textBrowser_errNewClient.setStyleSheet(style)
        self.timer.singleShot(3000, lambda: self.ui.textBrowser_errNewClient.setText(""))

    def new_services(self):             #Добавление заказа в БД
        clientID = str(self.ui.lineEdit_clients.text())
        stat = str("На выполнении")
        date = str(datetime.date.today())
        info = self.ui.lineEdit_info.text()
        summ = str(self.ui.lineEdit_sum.text())
        if clientID == "" or info == "" or summ == "":
            string = "Ошибка"
        else:
            self.APIBD.new_service(int(clientID), info, date, stat, int(summ))
            string = "Успешно"

        self.ui.textBrowser_errNewOrder.setText(string)
        style = ("font: 87 10pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui.textBrowser_errNewOrder.setStyleSheet(style)
        self.timer.singleShot(3000, lambda: self.ui.textBrowser_errNewOrder.setText(""))

    def checkOrders(self):            #Внесение в таблицу информации с БД (Заказы)
        find = str(self.ui.lineEdit_findOrders.text())
        if str == "":
            OrdersIDs = self.APIBD.show_all_service()
        else:
            OrdersIDs = self.APIBD.findOrders(find)
        print("Таблица заказов обновлена")
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget_2.setRowCount(len(OrdersIDs))
        self.ui.tableWidget_2.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        for i in range(len(OrdersIDs)):
            for j in range(5):
                if j == 0:
                    save = str(OrdersIDs[i][j])
                    #print(save)
                if j < 4:
                    self.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(OrdersIDs[i][j])))
                else:
                    prints = "Заказ №" + save
                    button = QtWidgets.QPushButton(prints)
                    button.setStyleSheet("background-color: white; border-radius: 3px; margin: 3px;")
                    button.clicked.connect(lambda _, row=save: self.openInterfaceOrders(row))
                    self.ui.tableWidget_2.setCellWidget(i, j, button)

        headers = ['№', 'ФИО', 'Статус', 'Дата', 'Инфо/управление']
        self.ui.tableWidget_2.setHorizontalHeaderLabels(headers)

        self.ui.textBrowser_errCheckOrders.setText("Обновлено")
        style = ("font: 87 10pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui.textBrowser_errCheckOrders.setStyleSheet(style)
        self.timer.singleShot(3000, lambda: self.ui.textBrowser_errCheckOrders.setText(""))

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

    def checkClients(self):            #Внесение в таблицу информации с БД (Клиенты)
        find = str(self.ui.lineEdit_2.text())
        if str == "":
            ClientsIDs = self.APIBD.show_all_service()
        else:
            ClientsIDs = self.APIBD.findClients(find)
        print(len(ClientsIDs))
        self.ui.tableWidget_3.clear()
        self.ui.tableWidget_3.setRowCount(len(ClientsIDs))
        self.ui.tableWidget_3.setSelectionMode(QtWidgets.QTableWidget.NoSelection)
        for i in range(len(ClientsIDs)):
            for j in range(6):
                if j == 0:
                    save = str(ClientsIDs[i][j])
                    print(save)
                if j < 5:
                    self.ui.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(ClientsIDs[i][j])))
                else:
                    prints = "Управление №" + save
                    button = QtWidgets.QPushButton(prints)
                    button.setStyleSheet("background-color: white; border-radius: 3px; margin: 3px;")
                    button.clicked.connect(lambda _, row=save: self.openInterfaceClients(row))
                    self.ui.tableWidget_3.setCellWidget(i, j, button)

        self.ui.textBrowser_errCheckClients.setText("Обновлено")
        style = ("font: 87 10pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui.textBrowser_errCheckClients.setStyleSheet(style)
        self.timer.singleShot(3000, lambda: self.ui.textBrowser_errCheckClients.setText(""))

    def openInterfaceClients(self, row):
        self.clients_interface = QtWidgets.QMainWindow()
        self.ui_client = Ui_ClientDialog()
        self.ui_client.setupUi(self.clients_interface)
        self.clients_interface.show()

        InfoID = self.APIBD.showClientDialog(row)

        html_text = "<div align='center'>Клиент:</div><div align='center'>" + str(InfoID[0][0]) + "</div>"
        self.ui_client.TextClient_FIO.setText(html_text)

        html_text = "<div align='center'>Телефон:</div><div align='center'>" + str(InfoID[0][1]) + "</div>"
        self.ui_client.TextClient_num.setText(html_text)

        html_text = "<div align='center'>Почта:</div><div align='center'>" + str(InfoID[0][2]) + "</div>"
        self.ui_client.TextClient_email.setText(html_text)

        html_text = "<div align='center'>Дата:</div><div align='center'>" + str(InfoID[0][3]) + "</div>"
        self.ui_client.TextClient_date.setText(html_text)

        # Доп. настройка стилей
        style = ("font: 87 12pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui_client.TextClient_FIO.setStyleSheet(style)
        self.ui_client.TextClient_num.setStyleSheet(style)
        self.ui_client.TextClient_email.setStyleSheet(style)
        self.ui_client.TextClient_date.setStyleSheet(style)











if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Work()
    myapp.show()
    sys.exit(app.exec())
