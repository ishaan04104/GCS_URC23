import matplotlib.pyplot as plt
import numpy as np

def getGraph():
# Data for different gases in ppm
    MQ3 = [960,960,960,960,960,960,960,960]
    MQ5 = [800,750,732,710,690,675,650,643]
    MQ6 = [400,380,375,356,345,321,300,298]


    # X-axis data for the plot
    Time = [0,1.2,2.5,3.3,4,5.2,6.4,7.1]

    # Create a figure and axis object
    fig, ax = plt.subplots()


    # Set the x-axis label and y-axis label
    ax.set_xlabel('Time(seconds)')
    ax.set_ylabel('Sensor reading (ppm)')

    # Set the title for the plot
    ax.set_title('Sensor Reading for Different Gases')

    # Loop through the data for each gas and plot each point with a delay
    for i in range(len(Time)):
        ax.plot(Time[i], MQ3[i], 'ro', label='MQ3')
        ax.plot(Time[i], MQ5[i], 'bo', label='MQ5')
        ax.plot(Time[i], MQ6[i], 'go', label='MQ6')
        
        # Add a delay of 0.5 seconds after each point is plotted
        plt.pause(1.0)

    # Connect the dots with a delay
    for i in range(len(Time) - 1):
        ax.plot([Time[i], Time[i+1]], [MQ3[i], MQ3[i+1]], 'r-', label='MQ3')
        ax.plot([Time[i], Time[i+1]], [MQ5[i], MQ5[i+1]], 'b-', label='MQ5')
        ax.plot([Time[i], Time[i+1]], [MQ6[i], MQ6[i+1]], 'g-', label='MQ6')
        
        # Add a delay of 0.5 seconds after each line is plotted
        plt.pause(1.0)

    ax.legend(["MQ3","MQ5","MQ6"], loc="lower right")

    # Display the plot
    plt.show()
