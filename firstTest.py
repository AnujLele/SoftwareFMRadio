from rtlsdr import rtlsdr
from SFMR_UI5 import Ui_MainWindow
import sys
from FMRadio import FMRadio
# sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
from PyQt5 import *
# from PyQt5 import Qt

# print("SYS PATH HERE" + str(sys.path))
mainApp = QtWidgets.QApplication([])
# gnuRadioapp = Qt.QApplication([])

# topblock = rtlsdr()

class functionalMainUI(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.radio = FMRadio()

    def connectFunctions(self):
        self.pushButton.clicked.connect(self.radio.startFMStation)



MainWindow = QtWidgets.QMainWindow()
ui = functionalMainUI()
ui.setupUi(MainWindow)
ui.connectFunctions()
MainWindow.show()

mainApp.exec()



