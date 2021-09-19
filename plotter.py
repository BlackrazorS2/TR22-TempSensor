import csv
import matplotlib
import matplotlib.pyplot as plt

dataSet = input("What is the file path of the dataset you want to plot?: ")
output_loc = input("Where do you want the graph to be saved to?(you can just press enter for here): ")
name = input("What do you want the file to be named?: ")
if name.strip() == "": # if the name is just a bunch of spaces or something
    name = "PlotterOut"

with open(dataSet,'r') as f_input:
    csv_input = csv.reader(f_input, delimiter=',', skipinitialspace=True)
    x_times = []
    ambientF = []
    objectF = []
    ambientC = []
    objectC = []

    next(csv_input)

    for cols in csv_input:
        x_times.append(matplotlib.dates.datestr2num(cols[0]))
        ambientF.append(float(cols[1]))
        objectF.append(float(cols[2]))
        ambientC.append(float(cols[3]))
        objectC.append(float(cols[4]))

plt.figure(figsize=(15,9), dpi=400)
# naming the x axis 
plt.xlabel('Real-Time') 
# naming the y axis 
plt.ylabel('Brake Temp') 
# giving a title to my graph 
plt.title('Brake Temp vs Time')
# plotting the points 
plt.plot_date(x_times, ambientF, "b-" , linewidth=2, markersize=1, label="Ambient Temp (*F)")

plt.plot_date(x_times, objectF, "r-" , linewidth=2, markersize=1, label="Target Temp (*F)")

plt.plot_date(x_times, ambientC, "k-" , linewidth=2, markersize=1, label="Ambient Temp (*C)")

plt.plot_date(x_times, objectC, "g-" , linewidth=2, markersize=1, label="Target Temp (*C)")
# adding the legend
plt.legend(loc="upper left")
# beautify the x-labels
plt.gcf().autofmt_xdate()
plt.grid()
plt.savefig(f"{output_loc}{name}.png", dpi=400)

# I just have this off for right now since its really big on the screen in order to get a good image saved
# function to show the plot 
#plt.show()
