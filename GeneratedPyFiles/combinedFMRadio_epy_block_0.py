"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, file_path = "/Users/anujlele/Documents/logFreq.txt", center_frequency = 96.9e6):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='EPB: Message to File',   # will show up in GRC
            in_sig=None,
            out_sig=None
        ) # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.message_port_register_in(pmt.intern('signalsDetected'))
        self.message_port_register_in(pmt.intern('centerFrequency'))
        self.set_msg_handler(pmt.intern('signalsDetected'), self.handle_message)
        self.set_msg_handler(pmt.intern('centerFrequency'), self.handle_message2)
        self.file_path = file_path
        self.centerFrequency = center_frequency
        
    def handle_message(self, msg):
        m = pmt.to_python(msg)
        message = str(m)
        signalIndex = message.rfind("array")
        while signalIndex != -1: # while "array" is found
            detectedFreqOffset = ""
            i = 7 # the index of the first digit we care about, singalIndex + "array[("
            while message[signalIndex + i] != ',':
                detectedFreqOffset += message[signalIndex + i]
                i += 1
            detectedFreq = int(float(detectedFreqOffset) + self.centerFrequency)
            with open(self.file_path, 'a') as f:
                f.write(str(detectedFreq) + "\n")
            
            message = message[:signalIndex]
            signalIndex = message.rfind("array")

    def handle_message2(self, msg):
        self.centerFrequency = float(pmt.to_python(msg))
            
    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = input_items[0]
        return len(output_items[0])
