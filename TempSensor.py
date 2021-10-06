# This basically is a gui hub for all the other programs
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import SerialReader
import plotter

# Initialize Tkinter
root = Tk()
root.title("Temp Sensing")
tabControl = ttk.Notebook(root)

def browseFile(tvar):
    tfile = fd.askopenfilename()
    tvar.delete(0, 'end')
    tvar.insert(0, tfile)

def browseDir(tvar):
    tfile = fd.askdirectory()
    tvar.delete(0, 'end')
    tvar.insert(0, tfile)
    
def changeLabel(label, text):
    """changes the text of a label"""
    label['text'] = text

def buttonEnable(*args):
    """makes sure all fields are full before allowing start button to be pressed"""
    x = target_type.get()
    y = target.get()
    if x and y:
        read_startButton.config(state='normal')
    else:
        read_startButton.config(state='disabled')


# Initializing frames for tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

# Initializing and placing tabs  
tabControl.add(tab1, text ='Read')
tabControl.add(tab2, text ='Plot')
tabControl.add(tab3, text ='Compare')
tabControl.pack(expand = 1, fill ="both")


################ Tab 1 ###################

# Initializing and placing labels
read_selectLabel = ttk.Label(tab1, text="Select type ")
read_selectLabel.grid(column=2,row=0)
read_statusLabel = ttk.Label(tab1, text="Idle")
read_statusLabel.grid(column=4, row=2)

# Initializing radiobuttonsfor selecting target type
target_type = StringVar()

ipText = "Enter IP address:"
ip = ttk.Radiobutton(tab1, text="IP", variable=target_type, value="IP", command=lambda: changeLabel(read_selectLabel, ipText))
serialText = "Enter serial port:"
serial = ttk.Radiobutton(tab1, text="Serial", variable=target_type, value="Serial", command=lambda: changeLabel(read_selectLabel, serialText))
fileText = "Enter file path or browse:"
file = ttk.Radiobutton(tab1, text="File", variable=target_type, value="File", command=lambda: changeLabel(read_selectLabel, fileText))
ip.grid(column=1, row = 1, sticky="W")
serial.grid(column=1, row = 2, sticky="W")
file.grid(column=1, row = 3, sticky="W")

# Initializing entry field and file browse button for selecting actual target
target = StringVar()
read_targetEntry = ttk.Entry(tab1, textvariable=target)
read_targetEntry.grid(column=2, row=1)
read_browseButton = ttk.Button(tab1, text="or browse for a file", command=lambda: browseFile(read_targetEntry))
read_browseButton.grid(column=2, row=2)

# Initialize observers
target_type.trace("w", buttonEnable)
target.trace("w", buttonEnable)

# Initializing Start button
read_startButton = ttk.Button(tab1, text="Start", command=lambda: SerialReader.read(target_type.get(), read_statusLabel, target.get()))#, state="disabled")
read_startButton.grid(column=4, row=1)

########### End of Tab 1 ############


############### Tab 2 ###############

# Initialize Labels
plot_selectLabel = ttk.Label(tab2, text="Select File")
plot_selectLabel.grid(column=0, row=0, sticky="W")
plot_statusLabel = ttk.Label(tab2, text="Idle")
plot_statusLabel.grid(column=2, row=5, sticky="W")
plot_pathLabel = ttk.Label(tab2, text="Select output folder")
plot_pathLabel.grid(column=0, row=2, sticky="W")
plot_nameLabel = ttk.Label(tab2, text="Enter file name")
plot_nameLabel.grid(column=0, row=4, sticky="W")

# Initialize File Selection
data = StringVar()
plot_dataEntry = ttk.Entry(tab2, textvariable=data)
plot_dataEntry.grid(column=0, row=1, sticky="W")
plot_dataBrowse = ttk.Button(tab2, text="Browse", command=lambda: browseFile(plot_dataEntry))
plot_dataBrowse.grid(column=1, row=1, sticky="W")

# Initialize Output path
plot_outPath = StringVar()
plot_outPathEntry = ttk.Entry(tab2, textvariable=plot_outPath)
plot_outPathEntry.grid(column=0, row=3, sticky="W")
plot_dirBrowse = ttk.Button(tab2, text="Browse", command=lambda: browseDir(plot_outPathEntry))
plot_dirBrowse.grid(column=1, row=3, sticky="W")

# Initialize Output name
plot_outName = StringVar()
plot_outNameEntry = ttk.Entry(tab2, textvariable=plot_outName)
plot_outNameEntry.grid(column=0, row=5, sticky="W")

# Initialize Start Button
plot_startButton = ttk.Button(tab2, text="Start", command=lambda: plotter.plot(data.get(), plot_outPath.get(), plot_outName.get(), plot_statusLabel))#, state="disabled")
plot_startButton.grid(column=1, row=5, sticky="W")

########### End of Tab 2 ############


############# Tab 3 #################

# Initialize Labels

# Initialize File selections

# Initialize Unit selection

# Initialize Axis selection

# Initialize Output path

# Initialize Output name

# Initialize Start button

########## End of Tab 3 #############

# Startup the window
root.mainloop()  

