import sys
sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
# from PyQt5 import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from rtlsdr import rtlsdr
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
        # self.pushButton.setClickable(True)

    def connectFunctions(self):
        self.pushButton.clicked.connect(self.radio.startFMStation)

        # self.pushButton.clicked.connect(self.printStatement)

    def printStatement(self):
        print("Here now")




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