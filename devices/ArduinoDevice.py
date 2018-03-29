from devices.LoggerDevice import LoggerDevice
import threading


class ArduinoDevice(LoggerDevice):

    def __init__(self):
        self.headers = ["PWM", "I1"]
        self.data = ['1', '2']


    def get_data(self):
        return self.data


