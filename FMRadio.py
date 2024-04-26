import sys
sys.path.insert(0, "/Users/anujlele/radioconda/lib/python3.10/site-packages")
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject
from combinedFMRadio import combinedFMRadio
import time


class FMRadio(QObject):
    def __init__(self) -> None:
        super().__init__()
        self.GNURadio = combinedFMRadio()
        self.GNURadio.set_playAudio(False)


    # firstSignal = pyqtSignal(list)
    def startFMStation(self, freq):
        self.GNURadio.set_centerFrequency(freq * (10**6))
        self.GNURadio.set_decimationFactor(10)
        self.GNURadio.set_playAudio(True)
        self.GNURadio.start()
        # self.GNURadio.show()

    def stopFMStation(self):
        self.GNURadio.stop()
        self.GNURadio.wait()
        

    candidateStations = pyqtSignal(list)
    progressValue = pyqtSignal(int)
    def scanSpectrum(self):
        open('/Users/anujlele/Documents/logFreq.txt', 'w').close() # Clear log file
        frequencies = [f for f in range(89,108,2)] # frequencies in MHz, spanning the FM spectrum
        duration = 3 # number of seconds per center frequency
        candidates = []

        start_time = time.time()
        for freq in frequencies:
            self.GNURadio.set_centerFrequency(freq*(10**6))
            self.GNURadio.set_minBandwidth(86000)
            self.GNURadio.set_playAudio(False)
            self.GNURadio.start()

            while (time.time() - start_time) < duration:
                pass # dead loop waiting

            start_time = time.time()

            self.GNURadio.stop()
            self.GNURadio.wait()

            self.progressValue.emit(freq)

        with open('/Users/anujlele/Documents/logFreq.txt', 'r') as file:
            for line in file:
                stationMHz = round(float(line)/(10**6), 1)
                candidates.append(str(stationMHz))

        candidates = list(set(candidates)) # remove duplicates
        candidates.sort(key=float) # sort the list by station value
        file.close()

        self.candidateStations.emit(candidates)


                

        


            
            
        

