# import random
# import serial
# import time
# arduino = serial.Serial(port='/dev/ttyACM1', baudrate=19200)

# time.sleep(2)

# def sensor():

#     pyjson = {}

#     # Moisture
#     data = arduino.readline().decode().replace('  \r\n','')

#     pyjson["Moisture"] = data

#     ## Gas
#     data = arduino.readline().decode().replace('\r\n','')

#     pyjson["Gas"] = data

#     ## DHT11
#     data = arduino.readline().decode().replace('\r\n','')

#     pyjson["DHT11"] = data

#     ## Humidity
#     data = arduino.readline().decode().replace('\r\n','')

#     pyjson["Humidity"] = data

#     ## pH
#     data = arduino.readline().decode().replace('\r\n','')

#     pyjson["pH"] = data

#     ## LDR

#     data = arduino.readline().decode().replace('\r\n','')

#     pyjson["LDR"] = data

#     return pyjson

# print(sensor())

# def triad():
#     #triad
#     pyjson = {}

#     arduino.write(str.encode("t"))

#     data = arduino.readline()
#     strdata = data.decode()
#     clean = strdata.replace(" ","")
#     cleanArr = clean.split(",")

#     pyjson['A'] = cleanArr[0]
#     pyjson['B'] = cleanArr[1]
#     pyjson['C'] = cleanArr[2]
#     pyjson['D'] = cleanArr[3]
#     pyjson['E'] = cleanArr[4]
#     pyjson['F'] = cleanArr[5]
#     pyjson['G'] = cleanArr[6]
#     pyjson['H'] = cleanArr[7]
#     pyjson['I'] = cleanArr[8]
#     pyjson['J'] = cleanArr[9]
#     pyjson['K'] = cleanArr[10]
#     pyjson['L'] = cleanArr[11]

#     pyjson['R'] = cleanArr[12]
#     pyjson['S'] = cleanArr[13]
#     pyjson['T'] = cleanArr[14]
#     pyjson['U'] = cleanArr[15]
#     pyjson['V'] = cleanArr[16]
#     pyjson['W'] = cleanArr[17]
#     return pyjson
# import random


# def sensor():
#     num_points = 8
#     x_values = [380,450,485,500,565,590,625,750]
#     y_values = [random.randint(1000,5000) for _ in range(num_points)]
    
#     data = {'x': x_values, 'y': y_values}
#     print(data)
#     return data

