#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import combinedFMRadio_epy_block_0 as epy_block_0  # embedded python block
import combinedFMRadio_epy_block_0_0 as epy_block_0_0  # embedded python block
import gnuradio.inspector as inspector
from gnuradio import qtgui
import sip
import osmosdr
import time



class combinedFMRadio(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "combinedFMRadio")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.threshold = threshold = -40
        self.samp_rate = samp_rate = 2e6
        self.playAudio = playAudio = True
        self.minBandwidth = minBandwidth = 75000
        self.decimationFactor = decimationFactor = 4
        self.centerFrequency = centerFrequency = 162.55e6
        self.bw = bw = 50e3

        ##################################################
        # Blocks
        ##################################################

        self._threshold_range = qtgui.Range(-80, 0, 5, -40, 200)
        self._threshold_win = qtgui.RangeWidget(self._threshold_range, self.set_threshold, "'threshold'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._threshold_win)
        self._centerFrequency_range = qtgui.Range(87e6, 200e6, 2e6, 162.55e6, 200)
        self._centerFrequency_win = qtgui.RangeWidget(self._centerFrequency_range, self.set_centerFrequency, "'centerFrequency'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._centerFrequency_win)
        self.rtlsdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.rtlsdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(centerFrequency, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(bw, 0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=(int(48e3 * 10 * decimationFactor)),
                decimation=int(samp_rate),
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimationFactor,
                taps=[],
                fractional_bw=0)
        self._minBandwidth_range = qtgui.Range(20000, 200000, 10000, 75000, 200)
        self._minBandwidth_win = qtgui.RangeWidget(self._minBandwidth_range, self.set_minBandwidth, "'minBandwidth'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._minBandwidth_win)
        self.inspector_signal_detector_cvf_0 = inspector.signal_detector_cvf(samp_rate, 1024, window.WIN_BLACKMAN_hARRIS, threshold, 0.95, False, 0.2, 0.0001, 75000, 'log')
        self.inspector_qtgui_sink_vf_0 = inspector.qtgui_inspector_sink_vf(
          samp_rate,
          1024,
          0,
          1,
          1,
          False
        )
        self._inspector_qtgui_sink_vf_0_win = sip.wrapinstance(self.inspector_qtgui_sink_vf_0.pyqwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._inspector_qtgui_sink_vf_0_win)
        self.epy_block_0_0 = epy_block_0_0.blk(is_Passed=playAudio)
        self.epy_block_0 = epy_block_0.blk(file_path="/Users/anujlele/Documents/logFreq.txt", center_frequency=centerFrequency)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(5)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1)
        self.blocks_message_strobe_1 = blocks.message_strobe(pmt.intern("TEST"), 1000)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.intern(str(playAudio)), 20)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern(str(centerFrequency)), 20)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=(samp_rate/decimationFactor),
        	audio_decimation=10,
        )


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.epy_block_0, 'centerFrequency'))
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.epy_block_0_0, 'Play_Audio?'))
        self.msg_connect((self.blocks_message_strobe_1, 'strobe'), (self.epy_block_0, 'signalsDetected'))
        self.msg_connect((self.inspector_qtgui_sink_vf_0, 'map_out'), (self.blocks_message_strobe_1, 'set_msg'))
        self.msg_connect((self.inspector_signal_detector_cvf_0, 'map_out'), (self.inspector_qtgui_sink_vf_0, 'map_in'))
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.epy_block_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.inspector_signal_detector_cvf_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.audio_sink_0, 1))
        self.connect((self.inspector_signal_detector_cvf_0, 0), (self.inspector_qtgui_sink_vf_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rational_resampler_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "combinedFMRadio")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.inspector_signal_detector_cvf_0.set_threshold(self.threshold)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.inspector_qtgui_sink_vf_0.set_samp_rate(self.samp_rate)
        self.inspector_signal_detector_cvf_0.set_samp_rate(self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_playAudio(self):
        return self.playAudio

    def set_playAudio(self, playAudio):
        self.playAudio = playAudio
        self.blocks_message_strobe_0_0.set_msg(pmt.intern(str(self.playAudio)))

    def get_minBandwidth(self):
        return self.minBandwidth

    def set_minBandwidth(self, minBandwidth):
        self.minBandwidth = minBandwidth

    def get_decimationFactor(self):
        return self.decimationFactor

    def set_decimationFactor(self, decimationFactor):
        self.decimationFactor = decimationFactor

    def get_centerFrequency(self):
        return self.centerFrequency

    def set_centerFrequency(self, centerFrequency):
        self.centerFrequency = centerFrequency
        self.blocks_message_strobe_0.set_msg(pmt.intern(str(self.centerFrequency)))
        self.rtlsdr_source_0.set_center_freq(self.centerFrequency, 0)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.rtlsdr_source_0.set_bandwidth(self.bw, 0)
        self.rtlsdr_source_0.set_bandwidth(self.bw, 1)




def main(top_block_cls=combinedFMRadio, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
