# This basically is a gui hub for all the other programs
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
#import SerialReader


root = Tk()
root.title("Temp Sensing")
tabControl = ttk.Notebook(root)

def browseFile(tvar):
    filename = fd.askopenfilename()
    return filename

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

#initializing and placing tabs  
tabControl.add(tab1, text ='Read')
tabControl.add(tab2, text ='Plot')
tabControl.add(tab3, text ='Compare')
tabControl.pack(expand = 1, fill ="both")
  
# initializing and placing labels
read_selectLabel = ttk.Label(tab1, text="Enter serial port")
read_selectLabel.grid(column=1,row=0)
read_outputLabel = ttk.Label(tab1, text="Data Read:")
read_outputLabel.grid(column=0, row=0)

# initializing and placing reader materials
target = StringVar()
read_targetEntry = ttk.Entry(tab1, textvariable=target)
read_targetEntry.grid(column=1, row=1)
read_browseButton = ttk.Button(tab1, text="or browse for a file", command=lambda target: browseFile())#browseFile)
read_browseButton.grid(column=1, row=2)



read_startButton = ttk.Button(tab1, text="Start")#, command=SerialReader)
read_startButton.grid(column=4, row=1)


  
root.mainloop()  

