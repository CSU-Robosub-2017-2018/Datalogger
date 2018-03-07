import datetime
from pathlib import Path

class csv:

    def __init__(self, filename):
        self.filename = filename.split('.')[0] + '00.CSV'
        self.fileopen = False

    def write(self, strarray):
        retstr = ','
        for i in range(0, len(strarray)-1):
            retstr = retstr + strarray[i] + ','
        retstr = retstr + strarray[len(strarray)-1]
        self.writer.write(retstr)

    def write_data(self, loggerlist=[]):
        self.write_time()
        for i in range(0, len(loggerlist)):
            self.write(loggerlist[i].get_data())
        self.write_newline()

    def write_time(self):
        self.writer.write(datetime.datetime.now().strftime("%H:%M:%S"))

    def write_newline(self):
        self.writer.write('\n')

    def write_headers(self, loggerlist=[]):
        self.write_date()
        for i in range(0, len(loggerlist)):
            self.write(loggerlist[i].get_headers())
        self.write_newline()

    def write_date(self):
        self.writer.write(datetime.datetime.now().strftime("%m/%d/%Y"))

    def open(self, loggerlist):
        if not self.fileopen:
            for i in range(0, 100):
                self.filename = self.filename[:-6] + str(int(i / 10)) + self.filename[-5:]
                self.filename = self.filename[:-5] + str(i % 10) + self.filename[-4:]
                my_file = Path(self.filename)
                if not my_file.is_file():
                    break
            self.writer = open(self.filename, "w")
            self.fileopen = True
            self.write_headers(loggerlist)
        else:
            print("[WARNING] Cannot open a file that is already open.")

    def close(self):
        if self.fileopen:
            self.writer.close()
            self.fileopen = False
        else:
            print("[WARNING] Cannot close a file that is not open.")



