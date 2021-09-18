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

There are currently 3 python files: `SerialReader`, `plotter`, and `Comparator`
All the files were written in python 3.7.2 but should be compatible with any python version above 3.6
    - If for whatever reason you want to use a python version before 3.6, replace all instances of f strings `f"{blah} words"` with the old string
    formatting `"{0} words".format(blah)`. I also cannot guarantee the stability of the other packages in older verisons.

**__SerialReader__** handles the data collection from the arduino be reading the output in a given serial port(usb).
Future implementations will likely need to be able to parse from a wireless connection - which if simple radios are used,
won't change how this program works at all

The output of `SerialReader` is a csv file as follows:

| Current Time (Date of Test) | Ambient Temperature (\*F) | Object Temperature (\*F) | Ambient Temperature (\*C) | Object Temperature (\*F) |
| :-------------------------- | :-----------------------: | :----------------------: | :-----------------------: | -----------------------: |
| Hours:Minutes:Seconds       |  Ambient Temp in F        |  Object Temp in F        |  Ambient Temp in C        |  Object Temp in C        |

**__plotter__** takes a csv file in the format output by `SerialReader` and uses matplotlib to create a graph of the data, saving it to whatever
location you want

**__Comparator__** takes two csv files in the format output by `SerialReader` and uses matplotlib to graph both sets of data against one another
in either degrees Celcius or degrees Fahrenheit. Just like `plotter`, `Comparator` takes the plot and saves it as an image wherever you want
so you can reference it in the future