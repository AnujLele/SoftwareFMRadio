from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
from PyQt5 import *
from rtlsdr import rtlsdr


class FMRadio():
    def __init__(self) -> None:
        self.gnuRadioapp = Qt.QApplication([])
        self.stationPlayer = rtlsdr()
        self.gnuRadioapp.exec()

    def startFMStation(self):
        self.stationPlayer.set_centerFrequency(96.9)
        self.stationPlayer.set_decimationFactor(10)
        self.stationPlayer.start()
        # self.stationPlayer.show()

    def scanSpectrum(self):
        pass
        

