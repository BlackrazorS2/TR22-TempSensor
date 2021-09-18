import csv
import matplotlib
import matplotlib.pyplot as plt

with open('DemoDataSet.csv','r') as f_input:
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

# naming the x axis 
plt.xlabel('Real-Time') 
# naming the y axis 
plt.ylabel('Brake Temp') 
# giving a title to my graph 
plt.title('Brake Temp vs Time')
# plotting the points 
plt.plot_date(x_times, ambientF, "b-" , linewidth=2, markersize=1)

plt.plot_date(x_times, objectF, "r-" , linewidth=2, markersize=1)

plt.plot_date(x_times, ambientC, "k-" , linewidth=2, markersize=1)

plt.plot_date(x_times, objectC, "g-" , linewidth=2, markersize=1)
# beautify the x-labels
plt.gcf().autofmt_xdate()
# function to show the plot 
plt.show()
