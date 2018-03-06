
class DataLogger:

    def __init__(self, FileWriter):
        self.running = False
        self.FileWriter = FileWriter
        self.devices = []

    def add_device(self, device):
        if not self.running:
            self.devices.append(device)
        else:
            print("[WARNING] Cannot add device while logger is running.")

    def start(self):
        if not self.running:
            self.running = True
            self.FileWriter.open(self.devices)
        else:
            print("[WARNING] Cannot start logger while logger is already running!")

    def end(self):
        self.running = False
        self.FileWriter.close()

    def log(self):
        self.FileWriter.write_data(self.devices)
