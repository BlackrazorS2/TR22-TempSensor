# Reads serial COM (usb) output from the arduino and exports it to csv to be used for later data processing
# Note that the data could be automatically exported to excel using PLX-DAQ but that's additional software to download+install
#       This method also allows for flexibility with data processing since we aren't bound by one format of exporting
# requires the pySerial package "pip install pyserial"
import csv
import serial
from os.path import exists
import datetime as dt
from datetime import datetime
import sys

source = input("Are we reading from serial or from an SD card?[s/c] ").lower()
while True:
    if source == "s" or source == "c":
        break
    else:
        continue
if source == "c":
    path = input("What is the absolute path to the file we are gathering data from? ")
# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = "COM3" # Change to whatever usb port you have the arduino plugged into
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600
date = datetime.now().strftime('%m/%d/%Y')
# Stuff so that we can make multiple data sets quickly
# Essentially will just name the datafile something different automatically if one already exists
data_set_counter = 1
while exists(f"TempData{data_set_counter}.csv"):
    data_set_counter += 1
# Sets up the headers for the csv file
with open(f"TempData{data_set_counter}.csv", "a+",newline='') as output:
    
    fieldNames = [f"Time ({date})", "Ambient (*F)", "Object (*F)", "Ambient (*C)", "Object (*C)"]
    writer = csv.DictWriter(output, fieldnames=fieldNames)
    writer.writeheader()

def main():
    if source == "s":
        ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    elif source == "c":
        sd = open(path, "r")
    while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        if source == "s":
            reading = ser.readline().decode('utf-8')
        elif source == "c":    
            reading = sd.readline()
        #print(reading)
        with open(f"TempData{data_set_counter}.csv", "a+", newline='') as output:
            fieldNames = [f"Time ({date})", "Ambient (*F)", "Object (*F)", "Ambient (*C)", "Object (*C)"]
            writer = csv.DictWriter(output, fieldnames=fieldNames)
            # We don't need to write headers since they've already been written above
        
            # Ok so mental plan is that the working time has a separate dilimiter
            # so you split the working time and the normal data

            try:
                try:
                    currentms, data = reading.split("|")
                    print(currentms)
                    currentTime = dt.timedelta(milliseconds=int(currentms))
                    print(currentTime)
                except Exception as e:
                    print(e)
                    currentTime = datetime.now().strftime('%H:%M:%S')
                    data = reading
                breakout = data.split(";")
                dataDict = {f"Time ({date})": currentTime, "Ambient (*F)": breakout[0], "Object (*F)": breakout[1], "Ambient (*C)": breakout[2], "Object (*C)": breakout[3]}
                writer.writerow(dataDict)
            except:
                print("Collected partial data, skipping...")
                continue

def exit():
    sys.exit()

if __name__ == "__main__":
    main()