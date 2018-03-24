import datetime

class FileWriter:

    def __init__(self, filename=None):
        self.filename = filename
        self.file = None

    def open(self):
        print("open")

    def close(self):
        print("close")

    def write(self):
        print("write")

