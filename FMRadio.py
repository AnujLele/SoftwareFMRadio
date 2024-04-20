import sys
sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal
from rtlsdr import rtlsdr
from peakDetector import peakDetector
import time


class FMRadio(object):
    def __init__(self) -> None:
        # self.stationPlayer = rtlsdr()
        self.spectrumScanner = peakDetector()
        # self.firstSignal = pyqtSignal()


    # firstSignal = pyqtSignal(list)
    def startFMStation(self):
        self.stationPlayer.set_centerFrequency(96.9e6)
        self.stationPlayer.set_decimationFactor(10)
        self.stationPlayer.start()
        self.stationPlayer.show()

        

    
    def scanSpectrum(self):

        freq = [f for f in range(89,108) if f%2 ==1]
        

        for f in freq:
            print("Here is the frequency" + str(f))
            self.spectrumScanner.set_centerFrequency(f * (10**6))
            self.spectrumScanner.start()
            self.spectrumScanner.wait()
            self.spectrumScanner.stop()

        candidateStations = []


        return candidateStations
            
            
        

