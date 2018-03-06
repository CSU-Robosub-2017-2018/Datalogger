from devices.LoggerDevice import LoggerDevice

class ArduinoDevice(LoggerDevice):

    def __init__(self):
        self.headers = ["test0", "test1"]
        self.int = 0

    def get_data(self):
        self.int += 1
        i = self.int % 7
        return [str(self.int), str(i)]