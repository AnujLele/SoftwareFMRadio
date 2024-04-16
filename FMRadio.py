import sys
sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal
from rtlsdr import rtlsdr


class FMRadio(object):
    def __init__(self) -> None:
        self.stationPlayer = rtlsdr()
        # self.firstSignal = pyqtSignal()


    # firstSignal = pyqtSignal(list)
    def startFMStation(self, freq=96.9e6):
        self.stationPlayer.set_centerFrequency(freq)
        self.stationPlayer.set_decimationFactor(10)
        self.stationPlayer.start()
        self.stationPlayer.show()

        

    
    def scanSpectrum(self):
        candidateStations = []


        return candidateStations
            
            
        

