from writers.csv import csv
from DataLogger import DataLogger
from time import sleep
from devices.ArduinoDevice import ArduinoDevice

writer = csv('testLog')
logger = DataLogger(writer)
logger.add_device(ArduinoDevice())
logger.start()

try:
    while True:
        print("hi")
        sleep(1)
finally:
    logger.end()
