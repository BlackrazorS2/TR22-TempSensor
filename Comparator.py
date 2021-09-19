# Compares two different temperature data sets - gui coming soon!
import csv
import matplotlib
import matplotlib.pyplot as plt
import datetime

print("Comparator creates a graph that compares two sets of temperature data in csv format:\n")
dataSet1 = input("Please enter the path of your first set of data: ")
set1Name = input("What would you like to call this dataset?: ")
print("\n")
dataSet2 = input("Please enter the path of your second set of data: ")
set2Name = input("What would you like to call this dataset?: ")
dest = input("Where would you like the graph to be saved to?: ")
outName = input("What do you want the graph to be called?: ")
if outName.strip() == "": # if the name is just spaces or something
    outName == "ComparatorOut"
print("\n")


unit = ""
while True:
    unit = input("Please enter whether you want to use degrees Celcius or degrees Fahrenheit[C\\F] ").upper()
    if unit == "F" or unit == "C":
        break
    else:
        continue

if unit == "F":
    a = 1
    o = 2
elif unit == "C":
    a = 3
    o = 4

# This should be in a function but copy paste is easier
# Data Set # 1
with open(dataSet1,'r') as data1:
    csv_input = csv.reader(data1, delimiter=',', skipinitialspace=True)
    x_times1 = [] # This will need to change from just time to delta time since start
    deltax1 = []
    ambient1 = []
    object1 = []

    next(csv_input)
    for cols in csv_input:
        x_times1.append(matplotlib.dates.datestr2num(cols[0])) # this is a float
        ambient1.append(float(cols[a]))
        object1.append(float(cols[o]))

    for i, x in enumerate(x_times1):
        if i == 0:
            deltax1.append(0)
        else:
            changex = x-x_times1[0]
            deltax1.append(changex)

# Data Set # 2
with open(dataSet2,'r') as data2:
    csv_input = csv.reader(data2, delimiter=',', skipinitialspace=True)
    x_times2 = [] # This will need to change from just time to delta time since start
    deltax2 = []
    ambient2 = []
    object2 = []

    next(csv_input)
    for cols in csv_input:
        x_times2.append(matplotlib.dates.datestr2num(cols[0])) # this is a float
        ambient2.append(float(cols[a]))
        object2.append(float(cols[o]))

    for i, x in enumerate(x_times2):
        if i == 0:
            deltax2.append(0)
        else:
            changex = x-x_times2[0]
            deltax2.append(changex)

plt.figure(figsize=(15,9), dpi=400)
# naming the x axis 
plt.xlabel('Delta T since start (H:M:S)') 
# naming the y axis 
plt.ylabel(f'Brake Temp (*{unit})') 
# giving a title to my graph 
plt.title('Brake Temp vs Time')
# plotting the points 
plt.plot_date(deltax1, ambient1, "b-" , linewidth=2, markersize=1, label=f"{set1Name} Ambient")

plt.plot_date(deltax1, object1, "r-" , linewidth=2, markersize=1, label=f"{set1Name} Target")

plt.plot_date(deltax2, ambient2, "k-" , linewidth=2, markersize=1, label=f"{set2Name} Ambient")

plt.plot_date(deltax2, object2, "g-" , linewidth=2, markersize=1, label=f"{set2Name} Target")
# adding the legend
plt.legend(loc="upper left")
# beautify the x-labels
plt.gcf().autofmt_xdate()
plt.grid()
plt.savefig(f"{dest}{outName}.png", dpi=400)

# I just have this off for right now since its really big on the screen in order to get a good image saved
# function to show the plot 
#plt.show()


