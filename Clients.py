# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Clients.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ClientDialog(object):
    def setupUi(self, ClientDialog):
        ClientDialog.setObjectName("ClientDialog")
        ClientDialog.resize(800, 567)
        ClientDialog.setMinimumSize(QtCore.QSize(800, 567))
        ClientDialog.setMaximumSize(QtCore.QSize(800, 567))
        ClientDialog.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.centralwidget = QtWidgets.QWidget(ClientDialog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 801, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TextClient_FIO = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.TextClient_FIO.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"\n"
"")
        self.TextClient_FIO.setObjectName("TextClient_FIO")
        self.verticalLayout.addWidget(self.TextClient_FIO)
        self.TextClient_num = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.TextClient_num.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"\n"
"")
        self.TextClient_num.setObjectName("TextClient_num")
        self.verticalLayout.addWidget(self.TextClient_num)
        self.TextClient_email = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.TextClient_email.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"\n"
"")
        self.TextClient_email.setObjectName("TextClient_email")
        self.verticalLayout.addWidget(self.TextClient_email)
        self.TextClient_date = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.TextClient_date.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"\n"
"")
        self.TextClient_date.setObjectName("TextClient_date")
        self.verticalLayout.addWidget(self.TextClient_date)
        self.pushButton_delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete_2.setGeometry(QtCore.QRect(620, 500, 171, 31))
        self.pushButton_delete_2.setStyleSheet("border-radius: 10%;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_delete_2.setObjectName("pushButton_delete_2")
        self.pushButton_delete_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete_3.setGeometry(QtCore.QRect(10, 500, 171, 31))
        self.pushButton_delete_3.setStyleSheet("border-radius: 10%;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_delete_3.setObjectName("pushButton_delete_3")
        self.pushButton_delete_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete_4.setGeometry(QtCore.QRect(320, 500, 171, 31))
        self.pushButton_delete_4.setStyleSheet("border-radius: 10%;\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_delete_4.setObjectName("pushButton_delete_4")
        ClientDialog.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ClientDialog)
        self.statusbar.setObjectName("statusbar")
        ClientDialog.setStatusBar(self.statusbar)

        self.retranslateUi(ClientDialog)
        QtCore.QMetaObject.connectSlotsByName(ClientDialog)

    def retranslateUi(self, ClientDialog):
        _translate = QtCore.QCoreApplication.translate
        ClientDialog.setWindowTitle(_translate("ClientDialog", "MainWindow"))
        self.TextClient_FIO.setHtml(_translate("ClientDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.TextClient_num.setHtml(_translate("ClientDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.TextClient_email.setHtml(_translate("ClientDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.TextClient_date.setHtml(_translate("ClientDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_delete_2.setText(_translate("ClientDialog", "Изменить"))
        self.pushButton_delete_3.setText(_translate("ClientDialog", "Удалить Клиента"))
        self.pushButton_delete_4.setText(_translate("ClientDialog", "Добавить в ЧС"))
