from devices.LoggerDevice import LoggerDevice
from 
import threading
import serial


class ArduinoDevice(LoggerDevice):

    def __init__(self):
        self.headers = ["PWM", "I1", "I2", "I3", "I4", "I5", "I6", "V", "StrainTop0",
                        "StrainTop45", "StrainTop90", "StrainSide0", "StrainSide45", "StrainSide90"]
        for i in range(0, 15):
            self.headers.append(("Therm" + str(i)))
        self.data = None
        self.serial = serial.Serial(helpers.find_arduino())
        self.thread = threading.Thread(target=self.update_data, args=())
        self.thread.daemon = True  # Daemonize thread
        self.thread.start()


    def update_data(self):
        while True:
            self.data = str(self.serial.read())[2:-1].split(',')[1:]#FIXME Find the number of bytes that will be sent



