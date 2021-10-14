# TR22-TempSensor
Temperature sensor code to monitor brake calipers on TR22

This is a simple arduino program using a slightly modified version of the demo code given by adafruit

The sensor used is the gy 609 ir temperature sensor and uses the adafruit MLX90614 library

The demo data set is me holding the ir sensor in the air, then putting it up to my monitor, then up to a cup that had been in the refrigerator

## Python

Python handles all the data collection from the arduino and post processing.

### Required packages

`datetime` - for tracking how long its been in between data captures
`csv` - for exporting and manipulating data
`pyserial` - for reading the data output by the arduino
`matplotlib` for graphing the data

## Files

There are currently 4 python files: `TempSensor`, `SerialReader`, `plotter`, and `Comparator`
All the files were written in python 3.8.5 but should be compatible with any python version above 3.6
    - If for whatever reason you want to use a python version before 3.6, replace all instances of f strings `f"{blah} words"` with the old string
    formatting `"{0} words".format(blah)`. I also cannot guarantee the stability of the other packages in older verisons.

__**SerialReader**__ handles the data collection from the arduino be reading the output in a given serial port(usb) or from a given text file
with the format of `time|AmbientF;ObjectF;AmbientC;ObjectC;`. Note that while `TempSensor` lists functionality over IP, this is not yet 
implemented and will not yield any output.

The output of `SerialReader` is a csv file as follows:

| Current Time (Date of Test) | Ambient Temperature (\*F) | Object Temperature (\*F) | Ambient Temperature (\*C) | Object Temperature (\*C) |
| :-------------------------- | :-----------------------: | :----------------------: | :-----------------------: | -----------------------: |
| Hours:Minutes:Seconds       |  Ambient Temp in F        |  Object Temp in F        |  Ambient Temp in C        |  Object Temp in C        |

__**plotter**__ takes a csv file in the format output by `SerialReader` and uses matplotlib to create a graph of the data, saving it to whatever
location you want

__**Comparator**__ takes two csv files in the format output by `SerialReader` and uses matplotlib to graph both sets of data against one another
in either degrees Celcius or degrees Fahrenheit. Just like `plotter`, `Comparator` takes the plot and saves it as an image wherever you want
so you can reference it in the future

__**TempSensor**__ is the GUI head for all the other programs. It contains multiple tabs, which each control one of the three other programs
for processing temperature data. For all fields that involve selecting files, either the file path can be typed in or the browse buttons can be
used to open a standard file explorer dialog box. Please ensure that all required fields are entered prior to selecting the start button; the 
program shouldn't (tm) hang, and you should be able to just correct the mistake and try again, but no output will be recieved if input was done
incorrectly. 
- Error tracking is currently in development.
- Note that on the `Read` tab there is a radiobutton for reading from IP. This button is currently not functional and will **NOT** do anything.