# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PasswordManager(object):
    def setupUi(self, PasswordManager):
        PasswordManager.setObjectName("PasswordManager")
        PasswordManager.resize(802, 563)
        self.centralwidget = QtWidgets.QWidget(PasswordManager)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 40, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(20)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 380, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        PasswordManager.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PasswordManager.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PasswordManager)
        self.statusbar.setObjectName("statusbar")
        PasswordManager.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PasswordManager)
        QtCore.QMetaObject.connectSlotsByName(PasswordManager)

    def retranslateUi(self, PasswordManager):
        _translate = QtCore.QCoreApplication.translate
        PasswordManager.setWindowTitle(_translate("PasswordManager", "MainWindow"))
        self.label.setText(_translate("PasswordManager", "PASSWORD MANAGER"))
        self.pushButton.setText(_translate("PasswordManager", "LOGIN"))
        self.label_2.setText(_translate("PasswordManager", "- HW Tech Club"))
        self.menuFile.setTitle(_translate("PasswordManager", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordManager = QtWidgets.QMainWindow()
    ui = Ui_PasswordManager()
    ui.setupUi(PasswordManager)
    PasswordManager.show()
    sys.exit(app.exec_())
