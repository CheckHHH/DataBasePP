# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\rabota\interface\Orders.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Order(object):
    def setupUi(self, Order):
        Order.setObjectName("Order")
        Order.resize(800, 567)
        Order.setMinimumSize(QtCore.QSize(800, 567))
        Order.setMaximumSize(QtCore.QSize(800, 567))
        Order.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.TextOrder_id = QtWidgets.QTextBrowser(Order)
        self.TextOrder_id.setGeometry(QtCore.QRect(0, 10, 801, 51))
        self.TextOrder_id.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"\n"
"")
        self.TextOrder_id.setObjectName("TextOrder_id")
        self.textBrowser_info = QtWidgets.QTextBrowser(Order)
        self.textBrowser_info.setGeometry(QtCore.QRect(0, 140, 801, 351))
        self.textBrowser_info.setObjectName("textBrowser_info")
        self.pushButton_cancel = QtWidgets.QPushButton(Order)
        self.pushButton_cancel.setGeometry(QtCore.QRect(320, 520, 171, 31))
        self.pushButton_cancel.setStyleSheet("border-radius: 10%;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_complete = QtWidgets.QPushButton(Order)
        self.pushButton_complete.setGeometry(QtCore.QRect(10, 520, 171, 31))
        self.pushButton_complete.setStyleSheet("border-radius: 10%;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_complete.setObjectName("pushButton_complete")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Order)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 801, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser_FIO = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_FIO.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"text-align: center;\n"
"\n"
"")
        self.textBrowser_FIO.setObjectName("textBrowser_FIO")
        self.horizontalLayout.addWidget(self.textBrowser_FIO)
        self.textBrowser_date = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_date.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"\n"
"")
        self.textBrowser_date.setObjectName("textBrowser_date")
        self.horizontalLayout.addWidget(self.textBrowser_date)
        self.textBrowser_sum = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser_sum.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"\n"
"")
        self.textBrowser_sum.setObjectName("textBrowser_sum")
        self.horizontalLayout.addWidget(self.textBrowser_sum)
        self.pushButton_delete = QtWidgets.QPushButton(Order)
        self.pushButton_delete.setGeometry(QtCore.QRect(620, 520, 171, 31))
        self.pushButton_delete.setStyleSheet("border-radius: 10%;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 106, 108);")
        self.pushButton_delete.setObjectName("pushButton_delete")

        self.retranslateUi(Order)
        QtCore.QMetaObject.connectSlotsByName(Order)

    def retranslateUi(self, Order):
        _translate = QtCore.QCoreApplication.translate
        Order.setWindowTitle(_translate("Order", "Заказ"))
        self.TextOrder_id.setHtml(_translate("Order", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI Black\'; font-size:22pt;\">Заказ № </span></p></body></html>"))
        self.textBrowser_info.setHtml(_translate("Order", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_cancel.setText(_translate("Order", "Отменить заказ"))
        self.pushButton_complete.setText(_translate("Order", "Завершить заказ"))
        self.textBrowser_FIO.setHtml(_translate("Order", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI Black\'; font-size:12pt;\">Клиент:</span></p></body></html>"))
        self.textBrowser_date.setHtml(_translate("Order", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI Black\'; font-size:12pt;\">Дата:</span></p></body></html>"))
        self.textBrowser_sum.setHtml(_translate("Order", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI Black\'; font-size:12pt;\">Стоимость:</span></p></body></html>"))
        self.pushButton_delete.setText(_translate("Order", "Удалить заказ"))
