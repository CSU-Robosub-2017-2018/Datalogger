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
        logger.log()
        print("log")
        sleep(.5)
finally:
    logger.end()
