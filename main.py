from design import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


def main():
    init_gui()
    

def init_gui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
