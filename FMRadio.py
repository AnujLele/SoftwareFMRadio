import sys
sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
from PyQt5 import Qt
from rtlsdr import rtlsdr


class FMRadio():
    def __init__(self) -> None:
        self.stationPlayer = rtlsdr()


    def startFMStation(self):
        self.stationPlayer.set_centerFrequency(96.9e6)
        self.stationPlayer.set_decimationFactor(10)
        self.stationPlayer.start()
        self.stationPlayer.show()


    def scanSpectrum(self):
        pass
        

