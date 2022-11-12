import numpy as np
import pandas as pd
from signal_generator import Signal
import statistics


class Drawing:
    def get_data_frame(self, graph_type, signal_type,GSR):

        # TODO: GET The target Signal
        signal = Signal.getSignal(signal_type,GSR)
        

        if graph_type == 1:
            return self.x_bar_chart_calculations(signal)
        else:
            return self.r_chart_calculations(signal)

    def x_bar_chart_calculations(self, signal):
        r_chart_calc=self.r_chart_calculations(signal)
        r_mean=r_chart_calc[2]
        samples_list=self.sample_signal(signal)
        alarm_flag=False
        x_bar_list=[]
        for sample in samples_list:
            x_bar_list.append(sample.mean())
        upper_limit= statistics.mean(x_bar_list)+0.31*r_mean
        lower_limit=statistics.mean(x_bar_list)-0.31*r_mean
        mean_line=statistics.mean(x_bar_list)

        for x_bar_value in x_bar_list:
            if x_bar_value>upper_limit or x_bar_value<lower_limit:
                alarm_flag=True

        return x_bar_list,upper_limit,mean_line,lower_limit,alarm_flag

    def r_chart_calculations(self, signal):
        samples_list=self.sample_signal(signal)
        alarm_flag=False
        r_list=[]
        for sample in samples_list:
            r_list.append(sample.max()-sample.min())
        upper_limit= 1.78*statistics.mean(r_list)
        lower_limit=0.22*statistics.mean(r_list)
        mean_line=statistics.mean(r_list)

        for r_value in r_list:
            if r_value>upper_limit or r_value<lower_limit:
                alarm_flag=True
        return r_list,upper_limit,mean_line,lower_limit,alarm_flag

    def sample_signal(self,signal):
        """
        Sampling continous signal to samples list with sample size=10
        """
        signal = signal[::5]
        combined_samples=[]
        for i in range(0,len(signal),10):
            one_sample_list=signal[i:i+10]
            combined_samples.append(one_sample_list)
        return combined_samples

