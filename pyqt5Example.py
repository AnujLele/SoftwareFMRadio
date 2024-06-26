import sys
sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
# from PyQt5 import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import pyqtSignal
# from rtlsdr import rtlsdr
from SFMR_UI5 import Ui_MainWindow
from FMRadio import FMRadio

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# stationPlayer = rtlsdr()
# stationPlayer.set_centerFrequency(96.9e6)
# stationPlayer.start()
# topBlock.show()

class functionalMainUI(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.radio = FMRadio()

    def connectFunctions(self):
        self.pushButton.clicked.connect(self.playStation)
        self.pushButton_7.clicked.connect(self.radio.scanSpectrum)
        self.pushButton_2.clicked.connect(self.stopStation)
        self.pushButton_7.clicked.connect(self.progressBar.reset)
        self.radio.candidateStations.connect(self.fillStations)
        self.radio.progressValue.connect(self.updateProgressBar)

    def fillStations(self, candidates):
        self.listWidget.clear()
        self.listWidget.addItems(candidates)

    def updateProgressBar(self, value):
        self.progressBar.setValue(value)

    def playStation(self):
        self.radio.startFMStation(float(self.listWidget.currentItem().text()))
        self.lcdNumber.display(float(self.listWidget.currentItem().text()))
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(False)

    def stopStation(self):
        self.radio.stopFMStation()
        self.pushButton_2.setDisabled(True)
        self.pushButton.setDisabled(False)


        






# Create a Qt widget, which will be our window.
window = QMainWindow()
ui = functionalMainUI()
ui.setupUi(window)
ui.connectFunctions()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.