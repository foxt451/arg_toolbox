from PyQt5 import QtWidgets, uic
from layouts_py import main_layout
import sys


def main():
	app = QtWidgets.QApplication([])
	win = MainWindow()

	win.show()
	sys.exit(app.exec())


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = main_layout.Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == '__main__':
	main()