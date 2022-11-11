import numpy as np
import pandas as pd


class Drawing:
    def get_data_frame(self, graph_type, signal_type):
        x = [np.random.rand() for i in range(100)]
        y = np.sin(x)

        # TODO: GET The target Signal
        signal = pd.DataFrame({'x': x, 'y': y})

        if graph_type == 1:
            return self.x_bar_chart_calculations(signal)
        else:
            return self.x_bar_chart_range_calculations(signal)

    def x_bar_chart_calculations(self, signal):
        x = signal.iloc[:, 0]
        y = signal.iloc[:, 1]

        # TODO: Calculations

        return pd.DataFrame({
            "x": x,
            "y": y
        })

    def x_bar_chart_range_calculations(self, signal):
        x = signal.iloc[:, 0]
        y = signal.iloc[:, 1]

        # TODO: Calculations

        return pd.DataFrame({
            "x": x,
            "y": y
        })
