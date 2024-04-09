from rtlsdr import rtlsdr
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from SFMR_UI import Ui_MainWindow
import sys
sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
from PyQt5 import *
# from PyQt5 import Qt

mainApp = QApplication([])
gnuRadioapp = Qt.QApplication([])

topblock = rtlsdr()

def startFMStation(freq):
    topblock.set_centerFrequency(freq)
    topblock.set_decimationFactor(10)
    topblock.start()
    # topblock.show()

MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
startFMStation(96.9e6)
gnuRadioapp.exec()
mainApp.exec()



