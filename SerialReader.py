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
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        print(reading)
        with open(f"TempData{data_set_counter}.csv", "a+", newline='') as output:
            fieldNames = [f"Time ({date})", "Ambient (*F)", "Object (*F)", "Ambient (*C)", "Object (*C)"]
            writer = csv.DictWriter(output, fieldnames=fieldNames)
            # We don't need to write headers since they've already been written above
            try:
                breakout = reading.split(";")
                currentTime = datetime.now().strftime('%H:%M:%S')
                dataDict = {f"Time ({date})": currentTime, "Ambient (*F)": breakout[0], "Object (*F)": breakout[1], "Ambient (*C)": breakout[2], "Object (*C)": breakout[3]}
                writer.writerow(dataDict)
            except:
                print("Collected partial data, skipping...")
                continue

if __name__ == "__main__":
    main()