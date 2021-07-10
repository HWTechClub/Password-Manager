# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from mainmenu import Ui_MainWindow2
import json


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 247)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setMinimumSize(QtCore.QSize(0, 0))
        self.label2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.button1.clicked.connect(self.thirdscr)
    """
    This function is for button1(Verify master password). Is the password present in the JSON file is correct, then main Menu window will open up
    """

    def thirdscr(self):
        # code from 3rd screen
        with open('../passwords/jsons.json', 'r') as f:
            crypticPassword = json.load(f)

        if(self.textEdit.toPlainText() == crypticPassword[0]['crypticMasterPass']):
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow2()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
        else:
            print('password is wrong')
            self.label2.setText(f'Password is wrong, Please try again')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label2.setText(_translate("MainWindow", "Enter master password"))
        self.button1.setText(_translate(
            "MainWindow", "Verify master password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
