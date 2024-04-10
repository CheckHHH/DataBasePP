# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("border-radius: 40px;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"")
        self.tab_1.setObjectName("tab_1")
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox.setGeometry(QtCore.QRect(130, 60, 521, 431))
        self.groupBox.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"border-radius: 20%;")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_reg = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_reg.setGeometry(QtCore.QRect(140, 330, 249, 41))
        self.pushButton_reg.setStyleSheet("border-radius: 20px;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 20, 251, 300))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_FIO = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_FIO.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"\n"
"")
        self.lineEdit_FIO.setInputMask("")
        self.lineEdit_FIO.setText("")
        self.lineEdit_FIO.setMaxLength(32767)
        self.lineEdit_FIO.setFrame(True)
        self.lineEdit_FIO.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_FIO.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_FIO.setClearButtonEnabled(False)
        self.lineEdit_FIO.setObjectName("lineEdit_FIO")
        self.verticalLayout.addWidget(self.lineEdit_FIO)
        self.lineEdit_num = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_num.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"\n"
"")
        self.lineEdit_num.setInputMask("")
        self.lineEdit_num.setText("")
        self.lineEdit_num.setMaxLength(32767)
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.verticalLayout.addWidget(self.lineEdit_num)
        self.lineEdit_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_email.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"\n"
"")
        self.lineEdit_email.setInputMask("")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setMaxLength(32767)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)
        self.lineEdit_date = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_date.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"\n"
"")
        self.lineEdit_date.setInputMask("")
        self.lineEdit_date.setText("")
        self.lineEdit_date.setMaxLength(32767)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.verticalLayout.addWidget(self.lineEdit_date)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 761, 521))
        self.groupBox_2.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"border-radius: 20%;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 741, 501))
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"border-radius: 1%;\n"
"border: 0px;")
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("border-radius: 40px;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"")
        self.tab_4.setObjectName("tab_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(0, 14, 251, 20))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(250, 10, 31, 31))
        self.pushButton.setStyleSheet("border-radius: 10%;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 50, 741, 421))
        self.tableWidget_2.setMinimumSize(QtCore.QSize(741, 421))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(761, 421))
        self.tableWidget_2.setMouseTracking(False)
        self.tableWidget_2.setStyleSheet("background-color: rgb(102, 102, 102);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"")
        self.tableWidget_2.setAutoScrollMargin(16)
        self.tableWidget_2.setDragEnabled(False)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(33)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_input = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_input.setGeometry(QtCore.QRect(480, 430, 249, 41))
        self.pushButton_input.setStyleSheet("border-radius: 20px;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_input.setObjectName("pushButton_input")
        self.lineEdit_clients = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_clients.setGeometry(QtCore.QRect(12, 10, 231, 21))
        self.lineEdit_clients.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"\n"
"")
        self.lineEdit_clients.setInputMask("")
        self.lineEdit_clients.setText("")
        self.lineEdit_clients.setMaxLength(32767)
        self.lineEdit_clients.setFrame(True)
        self.lineEdit_clients.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_clients.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_clients.setClearButtonEnabled(False)
        self.lineEdit_clients.setObjectName("lineEdit_clients")
        self.lineEdit_info = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_info.setGeometry(QtCore.QRect(12, 60, 721, 311))
        self.lineEdit_info.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"\n"
"")
        self.lineEdit_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_info.setObjectName("lineEdit_info")
        self.lineEdit_sum = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_sum.setGeometry(QtCore.QRect(12, 392, 231, 21))
        self.lineEdit_sum.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border: 0px;\n"
"\n"
"")
        self.lineEdit_sum.setInputMask("")
        self.lineEdit_sum.setText("")
        self.lineEdit_sum.setMaxLength(32767)
        self.lineEdit_sum.setFrame(True)
        self.lineEdit_sum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_sum.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_sum.setClearButtonEnabled(False)
        self.lineEdit_sum.setObjectName("lineEdit_sum")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_reg.setText(_translate("MainWindow", "Внести"))
        self.lineEdit_FIO.setPlaceholderText(_translate("MainWindow", "ФИО"))
        self.lineEdit_num.setPlaceholderText(_translate("MainWindow", "Телефон"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "Почта"))
        self.lineEdit_date.setPlaceholderText(_translate("MainWindow", "Дата рождения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Регистрация"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Поиск"))
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Инфо"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Таблица заказов"))
        self.pushButton_input.setText(_translate("MainWindow", "Внести"))
        self.lineEdit_clients.setPlaceholderText(_translate("MainWindow", "Клиент"))
        self.lineEdit_info.setPlaceholderText(_translate("MainWindow", "Информация"))
        self.lineEdit_sum.setPlaceholderText(_translate("MainWindow", "Стоимость"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Внести заказ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Заказы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Клиенты"))
