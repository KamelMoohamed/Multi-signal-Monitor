import neurokit2 as nk
import numpy as np
from pyfirmata import Arduino ,util
import time
import pandas as pd

def get_realtime(GSR):
    sensorValue = 0
    gsr_average = 0
    i = 0
    time_lst=[]
    values_lst=[]

    while i<50:
        sum=0
        for j in range (60000):
            try:
                sensorValue=GSR.read()
                sum+=int(sensorValue*1000)
                gsr_average=sum/10
            except:
                print('Error Occured')
        try:
            v=int(gsr_average)
            time_lst.append(i*0.0005)
            values_lst.append(gsr_average)
        except:
            print('Error Occured')
        i+=1
    return(pd.DataFrame({'t':time_lst,'y':values_lst}))
        

class Signal:
    ti = np.array((-70, -15, 0, 15, 100))
    ai = np.array((1.2, -5, 30, -7.5, 0.75))
    bi = np.array((0.25, 0.1, 0.1, 0.1, 0.4))
    ti = np.random.normal(ti, np.ones(5) * 3)
    ai = np.random.normal(ai, np.abs(ai / 5))
    bi = np.random.normal(bi, np.abs(bi / 5))

    ecg_signal = np.zeros(600)
    ecg_data = nk.ecg_simulate(duration=30)[::5]
    rsp_data= nk.rsp_simulate(duration=30,respiratory_rate=30)[::5]
    rsp_signal=np.zeros(600)
    counter = 0


    def getSignal(type,GSR):
        Signal.generate_ecg()
        Signal.generate_rsp()

        if type==2:
            return Signal.ecg_signal
        elif type==3:
            return Signal.rsp_signal
        else:
            
            return get_realtime(GSR)

    def generate_ecg():
        Signal.ecg_signal = np.append(
            Signal.ecg_signal[5:], Signal.ecg_data[:5])
        Signal.ecg_data = np.append(
            Signal.ecg_data[5:], Signal.ecg_data[:5])

    
    def generate_rsp():
        Signal.rsp_signal = np.append(
            Signal.rsp_signal[5:], Signal.rsp_data[:5])
        Signal.rsp_data = np.append(
            Signal.rsp_data[5:], Signal.rsp_data[:5])





