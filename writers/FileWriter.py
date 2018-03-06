import datetime

class FileWriter:

    def __init__(self, filename=None):
        self.filename = filename
        self.file = None

    def write(self):
        print("write")

