# Reads serial COM (usb) output from the arduino and exports it to csv to be used for later data processing
# Note that the data could be automatically exported to excel using PLX-DAQ but that's additional software to download+install
#       This method also allows for flexibility with data processing since we aren't bound by one format of exporting
# requires the pySerial package "pip install pyserial"
import csv
import serial
from os.path import exists
from datetime import datetime

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = "COM3" # Change to whatever usb port you have the arduino plugged into
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600

# Stuff so that we can make multiple data sets quickly
# Essentially will just name the datafile something different automatically if one already exists
data_set_counter = 1
while exists(f"TempData{data_set_counter}.txt"): # maybe this needs to be a csv file?
    data_set_counter += 1

def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        with open(f"TempData{data_set_counter}.txt", "a+") as output:
            output.write(reading)
        # reading is a string...do whatever you want from here
        print(reading)


if __name__ == "__main__":
    main()