import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import functools
from General import DataBaseApi

import re

#Интерфейсы
from interface.Interface import Ui_MainWindow
from interface.Orders import Ui_Order
from interface.Clients import Ui_ClientDialog
from interface.Warning import Ui_Dialog


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
        #self.ui.comboBox_listClients.activated.connect(self.listClients)
        self.listClients()
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
        client = str(self.ui.comboBox_listClients.currentText())
        clientID = ''.join(filter(str.isdigit, client))
        stat = str("На выполнении")
        date = str(datetime.date.today())
        info = self.ui.lineEdit_info.text()
        summ = str(self.ui.lineEdit_sum.text())
        if clientID == "" or info == "" or summ == "":
            string = "Ошибка"
        else:
            self.APIBD.new_service(int(clientID), info, date, stat, int(summ))
            string = "Успешно"
            self.checkOrders()

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
        self.orders_interface = QtWidgets.QMainWindow()
        self.ui_order = Ui_Order()
        self.ui_order.setupUi(self.orders_interface)
        self.orders_interface.show()

        InfoID = self.APIBD.showOrderDialog(row)

        html_text = "<div align='center'>Заказ № " + row + "</div>"
        self.ui_order.TextOrder_id.setText(html_text)

        html_text = "<div align='center'>Клиент:</div><div align='center'>" + str(InfoID[0][0]) + "</div>"
        self.ui_order.textBrowser_FIO.setText(html_text)

        html_text = "<div align='center'>Дата:</div><div align='center'>" + str(InfoID[0][1]) + "</div>"
        self.ui_order.textBrowser_date.setText(html_text)

        html_text = "<div align='center'>Инфо:</div><div align='center'>" + str(InfoID[0][2]) + "</div>"
        self.ui_order.textBrowser_info.setText(html_text)

        html_text = "<div align='center'>Стоимость:</div><div align='center'>" + str(InfoID[0][3]) + "</div>"
        self.ui_order.textBrowser_sum.setText(html_text)

        if str(InfoID[0][4]) == "Завершён" or str(InfoID[0][4]) == "Отменён":
            self.ui_order.pushButton_complete.hide()
            self.ui_order.pushButton_cancel.hide()
            self.ui_order.pushButton_delete.setGeometry(QtCore.QRect(10, 520, 780, 31))

        #Доп. настройка стилей
        style = ("font: 87 12pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui_order.textBrowser_FIO.setStyleSheet(style)
        self.ui_order.TextOrder_id.setStyleSheet(style + "font: 87 22pt \"Segoe UI Black\";")
        self.ui_order.textBrowser_date.setStyleSheet(style)
        self.ui_order.textBrowser_info.setStyleSheet(style)
        self.ui_order.textBrowser_sum.setStyleSheet(style)

        delete_func = functools.partial(self.deleteOrders, row)
        self.ui_order.pushButton_delete.clicked.connect(delete_func)

        complete_str = "Завершён"
        complete_func = functools.partial(self.completeOrders, (row, complete_str))
        self.ui_order.pushButton_complete.clicked.connect(complete_func)

        cancel_str = "Отменён"
        complete_func = functools.partial(self.completeOrders, (row, cancel_str))
        self.ui_order.pushButton_cancel.clicked.connect(complete_func)

    def completeOrders(self, row, complete_str):
        self.warning_interface = QtWidgets.QMainWindow()
        self.ui_warning = Ui_Dialog()
        self.ui_warning.setupUi(self.warning_interface)
        self.warning_interface.show()

        html_text = "<div align='center'>Внимание: заказ приобретёт статус и его нельзя будет изменить</div>"
        self.ui_warning.textBrowser.setText(html_text)
        style = ("font: 87 13pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui_warning.textBrowser.setStyleSheet(style)

        self.ui_warning.pushButton_OK.clicked.connect(lambda: clickOK(row))
        self.ui_warning.pushButton_cancel.clicked.connect(self.warning_interface.close)

        def clickOK(row):
            self.APIBD.completeOrder(row[0], row[1])
            self.orders_interface.close()
            self.warning_interface.close()
            self.checkOrders()

            self.ui.textBrowser_errCheckOrders.setText("Заказ № " + row[0] + " завершён/отменён")
            style = ("font: 87 10pt \"Segoe UI Black\";\n"
                     "color: rgb(255, 255, 255);"
                     "border: 0px;")

            self.ui.textBrowser_errCheckClients.setStyleSheet(style)
            self.timer.singleShot(3000, lambda: self.ui.textBrowser_errCheckClients.setText(""))
    def deleteOrders(self, row):
        self.warning_interface = QtWidgets.QMainWindow()
        self.ui_warning = Ui_Dialog()
        self.ui_warning.setupUi(self.warning_interface)
        self.warning_interface.show()

        html_text = "<div align='center'>Внимание: данное действие не отменить, вы уверены?</div>"
        self.ui_warning.textBrowser.setText(html_text)
        style = ("font: 87 15pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")
        self.ui_warning.textBrowser.setStyleSheet(style)

        self.ui_warning.pushButton_OK.clicked.connect(lambda: clickOK(row))
        self.ui_warning.pushButton_cancel.clicked.connect(self.warning_interface.close)
        def clickOK(row):
            self.APIBD.deleteOrder(row)
            self.orders_interface.close()
            self.warning_interface.close()
            self.checkOrders()

            self.ui.textBrowser_errCheckOrders.setText("Заказ № " + row + " удалён")
            style = ("font: 87 10pt \"Segoe UI Black\";\n"
                    "color: rgb(255, 255, 255);"
                    "border: 0px;")

            self.ui.textBrowser_errCheckClients.setStyleSheet(style)
            self.timer.singleShot(3000, lambda: self.ui.textBrowser_errCheckClients.setText(""))

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

        headers = ['№', 'ФИО', 'Телефон', 'Почта', 'Дата рождения', 'Управление']
        self.ui.tableWidget_3.setHorizontalHeaderLabels(headers)

    def openInterfaceClients(self, row):
        self.clients_interface = QtWidgets.QMainWindow()
        self.ui_client = Ui_ClientDialog()
        self.ui_client.setupUi(self.clients_interface)
        self.clients_interface.show()
        self.ui_client.groupBox_change.hide()

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

        delete_func = functools.partial(self.deleteClients, row)
        self.ui_client.pushButton_deleteClient.clicked.connect(delete_func)

        change_func = functools.partial(self.changeClients, (row, ))
        self.ui_client.pushButton_changeClient.clicked.connect(change_func)

    def deleteClients(self, row):
        self.warning_interface = QtWidgets.QMainWindow()
        self.ui_warning = Ui_Dialog()
        self.ui_warning.setupUi(self.warning_interface)
        self.warning_interface.show()

        self.ui_warning.pushButton_OK.clicked.connect(lambda: clickOK(row))
        self.ui_warning.pushButton_cancel.clicked.connect(self.warning_interface.close)
        def clickOK(row):
            self.APIBD.deleteClient(row)
            self.clients_interface.close()
            self.warning_interface.close()
            self.checkOrders()
            self.checkClients()

            self.ui.textBrowser_errCheckClients.setText("Клиент № " + row + " удалён")
            style = ("font: 87 10pt \"Segoe UI Black\";\n"
                    "color: rgb(255, 255, 255);"
                    "border: 0px;")

            self.ui.textBrowser_errCheckClients.setStyleSheet(style)
            self.timer.singleShot(3000, lambda: self.ui.textBrowser_errCheckClients.setText(""))

    def changeClients(self, row, InfoID):
        self.ui_client.groupBox_change.show()
        self.ui_client.pushButton_changeCancel.clicked.connect(self.ui_client.groupBox_change.hide)

        change_func = functools.partial(self.acceptChangeClients, row)
        self.ui_client.pushButton_changeAccept.clicked.connect(change_func)

    def acceptChangeClients(self, row):
        FIO = str(self.ui_client.lineEdit_changeFIOClient.text())
        num = str(self.ui_client.lineEdit_changeNumClient.text())
        email = str(self.ui_client.lineEdit_changeEmailClient.text())
        date = str(self.ui_client.lineEdit_changeDateClient.text())
        self.APIBD.changeClient(FIO, num, email, date, row)
        self.ui_client.groupBox_change.hide()
        self.clients_interface.close()
        self.checkClients()

        self.ui.textBrowser_errCheckClients.setText("Клиент № " + row + " изменён")
        style = ("font: 87 10pt \"Segoe UI Black\";\n"
                 "color: rgb(255, 255, 255);"
                 "border: 0px;")

        self.ui.textBrowser_errCheckClients.setStyleSheet(style)
        self.timer.singleShot(3000, lambda: self.ui.textBrowser_errCheckClients.setText(""))

    def listClients(self):
        self.ui.comboBox_listClients.clear()
        UsersID = self.APIBD.listClient()
        for i in range(len(UsersID)):
            self.ui.comboBox_listClients.addItem(str(UsersID[i][0]) + " №" + str(UsersID[i][1]))














if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Work()
    myapp.show()
    sys.exit(app.exec())
