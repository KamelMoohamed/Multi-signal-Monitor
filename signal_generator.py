import neurokit2 as nk
import numpy as np
import time
import pandas as pd
import serial


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
    real_time_signal=np.zeros(600)
    counter = 0


    def getSignal(type):
        Signal.generate_ecg()
        Signal.generate_rsp()
        Signal.get_realtime()

        if type == 1 :
            return Signal.real_time_signal
        elif type==2:
            return Signal.ecg_signal
        else:
            return Signal.rsp_signal
            

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


    def get_realtime():
        arduino = serial.Serial(port='COM3', baudrate=115200)
        reads=[]
        for i in range(5):
            while True:
                counter=0
                dataBarCode = arduino.readline()
                if len(dataBarCode) >= 1 and counter<=5:
                    try:
                        number= int(dataBarCode.decode("utf-8"))
                        reads.append(number)
                        break
                    except:
                        continue
        arduino.close()
        
        Signal.real_time_signal = np.append(
            Signal.real_time_signal[5:], np.array(reads))

