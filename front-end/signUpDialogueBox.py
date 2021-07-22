# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import startPage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topic = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(11)
        self.topic.setFont(font)
        self.topic.setAlignment(QtCore.Qt.AlignCenter)
        self.topic.setObjectName("topic")
        self.verticalLayout.addWidget(self.topic)
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setObjectName("OKButton")
        self.verticalLayout.addWidget(self.OKButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.OKButton.clicked.connect(self.closeDialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.topic.setText(_translate(
            "MainWindow", "You have already signed up!"))
        self.OKButton.setText(_translate("MainWindow", "OK"))

    def closeDialog(self):
        print("exiting sfely")
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = startPage.Ui_PasswordManager()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
