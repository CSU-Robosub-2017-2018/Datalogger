import threading
from time import sleep


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
            self.thread = threading.Thread(target=self.log, args=())
            self.thread.daemon = True  # Daemonize thread
            self.thread.start()
        else:
            print("[WARNING] Cannot start logger while logger is already running!")

    def end(self):
        self.running = False
        self.FileWriter.close()

    def log(self):
        while self.running:
            self.FileWriter.write_data(self.devices)
            sleep(0.25)
