
class DataLogger:

    running = False

    def __init__(self, FileWriter):
        self.FileWriter = FileWriter

    def add_device(self,device):
        if not self.running:
            self.devices += device
        else:
            print("[WARNING] Cannot add device while logger is running.")

    def start(self):
        if not self.running:
            self.running = True
        else:
            print("[WARNING] Cannot start logger while logger is already running!")

    def end(self):
        self.running = False
