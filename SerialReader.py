# Reads serial COM (usb) output from the arduino and exports it to csv to be used for later data processing
# Note that the data could be automatically exported to excel using PLX-DAQ but that's additional software to download+install
#       This method also allows for flexibility with data processing since we aren't bound by one format of exporting
# requires the pySerial package "pip install pyserial"
import csv
import serial
from os.path import exists
import datetime as dt
from datetime import datetime
from tkinter import ttk

# This script needs to be reworked to have at least 3 different functions
#   one to read data from ip, one for serial, and one for file
# the organizing of data should be its own function too to condense code

def parseData(linedata, dataCounter, header=True):
    """This is meant to disconnect the actual parsing of data from its collection"""
    with open(f"TempData{dataCounter}.csv", "a+", newline='') as output:
        date = datetime.now().strftime('%m/%d/%Y')
        fieldNames = [f"Time ({date})", "Ambient (*F)", "Object (*F)", "Ambient (*C)", "Object (*C)"]
        writer = csv.DictWriter(output, fieldnames=fieldNames)
        if header:
            writer.writeheader()
        try:
            try:
                currentms, data = linedata.split("|")
                currentTime = dt.timedelta(milliseconds=int(currentms))
            except Exception as e:
                print(e)
                currentTime = datetime.now().strftime('%H:%M:%S')
                data = linedata
            breakout = data.split(";")
            dataDict = {f"Time ({date})": currentTime, "Ambient (*F)": breakout[0], "Object (*F)": breakout[1], "Ambient (*C)": breakout[2], "Object (*C)": breakout[3]}
            writer.writerow(dataDict)
        except:
            print("Collected partial data, skipping...")

def ipRead(targetIP, count):
    """Need socket for this"""
    pass

def serialRead(port, count):
    """basically the original SerialReader program"""
    SERIAL_PORT = port # Change to whatever usb port you have the arduino plugged into
    # be sure to set this to the same rate used on the Arduino
    SERIAL_RATE = 9600
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    reading =  ser.readline().decode('utf-8')
    head = True
    while reading != "":
        reading =  ser.readline().decode('utf-8')
        parseData(reading, count, header=head)
        head = False

def fileRead(file, count):
    """basically the original SerialReader program just reading from the file"""
    sd = open(file, "r")
    reading =  sd.readline()
    head = True
    while reading != "":
        reading =  sd.readline()
        parseData(reading, count, header=head)
        head = False


def read(format, statusLabel, target=None):
    """Basically the master controller for this thing"""
    data_set_counter = 1
    statusLabel['text'] = "Processing..."
    while exists(f"TempData{data_set_counter}.csv"):
        data_set_counter += 1
    if format== "IP":
        ipRead(target, data_set_counter)
    elif format == "Serial":
        serialRead(target, data_set_counter)
    elif format == "File":
        fileRead(target, data_set_counter)
    else:
        raise ValueError("Unknown reading format: Did you click a radiobutton?")
    statusLabel['text'] = "Done"