import numpy as np
import pandas as pd
from signal_generator import Signal


class Drawing:
    def get_data_frame(self, graph_type, signal_type,GSR):

        # TODO: GET The target Signal
        signal = Signal.getSignal(signal_type,GSR)
        

        if graph_type == 1:
            return self.x_bar_chart_calculations(signal)
        else:
            return self.x_bar_chart_range_calculations(signal)

    def x_bar_chart_calculations(self, signal):

        # TODO: Calculations

        return signal

    def x_bar_chart_range_calculations(self, signal):

        # TODO: Calculations

        return signal
