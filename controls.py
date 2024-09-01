import random
import serial
arduino = serial.Serial(port='/dev/ttyACM1', baudrate=9600)


# def imuData():
#     imuList = []
#     imu = {}

#     while True:
#         data = arduino.readline().decode().strip()
#         if data:
#             x, y, z = map(float, data.split(','))
#             # print("Acceleration in x-axis:", x)
#             # print("Acceleration in y-axis:", y)
#             # print("Acceleration in z-axis:", z)
#             key1 = 'x'
#             key2 = 'y'
#             key3 = 'z'
#             imu[key1] = x
#             imu[key2] = y
#             imu[key3] = z
#             imuList.append(imu)

#             return imuList

# def your_function():
#     list_of_dictionaries = []
#     for i in range(10):
#         dictionary = {}
#         key1 = 'latitude'
#         key2 = 'longitude'
#         value1 = random.randint(0, 100)
#         value2 = random.randint(0/dev/ttyACM1, 100)
#         dictionary[key1] = value1
#         dictionary[key2] = value2
#         list_of_dictionaries.append(dictionary)
#     return (list_of_dictionaries)

# def your_function():
#     list_of_dictionaries = []
#     for i in range(10):
#         dictionary = {}
#         key1 = 'latitude'
#         key2 = 'longitude'
#         lat_int = arduino.readline().decode().replace('\r\n', '')
#         lat_frac = arduino.readline().decode().replace('\r\n', '')
#         lon_int = arduino.readline().decode().replace('\r\n', '')
#         lon_frac = arduino.readline().decode().replace('\r\n', '')
#         value1 = lat_int + lat_frac
#         value2 = lon_int + lon_frac
#         dictionary[key1] = value1
#         dictionary[key2] = value2
#         list_of_dictionaries.append(dictionary)
#     return (list_of_dictionaries)


# def your_function():
#     return [{'latitude': 12.967972167, 'longitude': 79.157240319}, {'latitude': 12.967960840, 'longitude': 79.157253030}, {'latitude': 12.967946081, 'longitude': 79.157243372}, {'latitude': 12.967977387, 'longitude': 79.157250901}, {'latitude': 12.967977415, 'longitude': 79.157263613}, {'latitude': 12.967966772, 'longitude': 79.157262963}, {'latitude': 12.967954916, 'longitude': 79.157262103}, {'latitude': 12.967944802, 'longitude': 79.157246361}, {'latitude': 12.967935921, 'longitude': 79.157249767}, {'latitude': 12.967937792, 'longitude': 79.157234036}, {'latitude': 12.967937752, 'longitude': 79.157233322}, {'latitude': 12.967936886, 'longitude': 79.157229916}, {'latitude': 12.967944314, 'longitude': 79.157225639}, {'latitude': 12.967942824, 'longitude': 79.157230387}, {'latitude': 12.967939575, 'longitude': 79.157229294},]

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def get_plot():
    # plot a separate point
    plt.plot(79.99, 12.000011, 'bo', label='destination')
    plt.text(79.99 + 0.1, 12.000011 + 0.1, "destination", fontsize=8)

    plt.pause(5)

    # data to plot
    data = [{'latitude': 12.000001, 'longitude': 79}, {'latitude': 12.000001, 'longitude': 79.12}, {'latitude': 12.000004, 'longitude': 79.24}, {'latitude': 12.000003, 'longitude': 79.36}, {'latitude': 12.000005, 'longitude': 79.48}, {'latitude': 12.000006, 'longitude': 79.6}, {'latitude': 12.000007, 'longitude': 79.72}, {'latitude': 12.000008, 'longitude': 79.84}, {'latitude': 12.000009, 'longitude': 79.96}, {'latitude': 12.000010, 'longitude': 79.961}, {'latitude': 12.000011, 'longitude': 79.99}]
    
    # plot data points
    for i in range(len(data)):
        plt.plot(data[i]['longitude'], data[i]['latitude'], 'ro', label='Data Points')
        plt.text(data[i]['longitude'] + 0.1, data[i]['latitude'] + 0.1, f"({data[i]['longitude']}, {data[i]['latitude']})", fontsize=8)
        if i > 0:
            plt.plot([data[i-1]['longitude'], data[i]['longitude']], [data[i-1]['latitude'], data[i]['latitude']], 'b')
        plt.pause(5)  # add a pause of 2 seconds to slow down the plot
    
    # add axis labels and title
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Data Points')

    # show the plot
    plt.legend()
    plt.show()



# your_function()

def wheels(var):
    if (var == 'F'):  # if the value is f
        print("forward")
    if (var == 'B'):  # if the value is b
        print("backward")
    if (var == 'L'):  # if the value is l
        print("left")
    if (var == 'R'):  # if the value is r
        print("right")
    if (var == 'S'):  # if the value is s
        print("stop")
    if (var == 'x'):
        print("partiaLeft")
    if (var == 'y'):
        print("partialRight")
    arduino.write(str.encode(var))

    # /dev/ttyACM1
