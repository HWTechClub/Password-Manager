from enterPassword import *

import sys


class EnterPassword(Ui_MainWindow1):
    def __init__(self, window):
        self.setupUi(window)
        self.button1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print('heyyo')


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = EnterPassword(MainWindow)

MainWindow.show()
app.exec_()
