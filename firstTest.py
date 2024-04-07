from rtlsdr import rtlsdr
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from SFMR_UI import Ui_MainWindow
import sys
# sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
# from PyQt5 import Qt

# app = Qt.QApplication([])

# topblock = rtlsdr()

# topblock.set_centerFrequency(162.55e6)
# topblock.set_decimationFactor(10)
# topblock.start()
# topblock.show()

# Start the event loop.
# app.exec()

# import sys
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec()



