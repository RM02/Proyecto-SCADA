import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Hmi.hmid import Ui_MainWindow

if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.modbus("192.168.10.2", 502)
	MainWindow.show()
	sys.exit(app.exec_())