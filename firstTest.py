from SFMR_UI import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from FMRadio import FMRadio

# sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
# from PyQt5 import *
# from PyQt5 import Qt


class functionalMainUI(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.radio = FMRadio()

    def connectFunctions(self):
        self.pushButton.clicked.connect(self.radio.startFMStation)
        # self.pushButton.clicked.connect(self.printStatement)

    def printStatement(self):
        print("Here now")



app = QtWidgets.QApplication([])
MainWindow = QtWidgets.QMainWindow()
ui = functionalMainUI()
ui.setupUi(MainWindow)
ui.connectFunctions()
MainWindow.show()
sys.exit(app.exec())
# gnuRadioapp = Qt.QApplication([])

# topblock = rtlsdr()

# def startFMStation(freq):
#     topblock.set_centerFrequency(freq)
#     topblock.set_decimationFactor(10)
#     topblock.start()
    # topblock.show()

# startFMStation(96.9e6)
# gnuRadioapp.exec_()






