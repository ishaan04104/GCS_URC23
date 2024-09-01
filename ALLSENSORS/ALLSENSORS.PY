import serial
arduino = serial.Serial(port='COM3', baudrate=9600)

def sensor():
    pyjson = {}

    #Triad
    data = arduino.readline()

    # Soil
    data = arduino.readline()
    strdata = data.decode()
    moisture_percentage = ( 100 - ( (float(strdata)/1023.00) * 100 ) )
    pyjson["soil"] = moisture_percentage

    # Gas 
    data = arduino.readline()
    strdata = data.decode().replace('\r\n','')
    pyjson["gas"] = strdata

    #DHT11
    data1 = arduino.readline()
    data2 = arduino.readline()

    pyjson["humidity"] = data1.decode().replace('\r\n','')
    pyjson["temperature"] = data2.decode().replace('\r\n','')

    return pyjson

def triad():
    #triad
    pyjson = {}

    data = arduino.readline()
    strdata = data.decode()
    clean = strdata.replace(" ","")
    cleanArr = clean.split(",")

    pyjson['A'] = cleanArr[0]
    pyjson['B'] = cleanArr[1]
    pyjson['C'] = cleanArr[2]
    pyjson['D'] = cleanArr[3]
    pyjson['E'] = cleanArr[4]
    pyjson['F'] = cleanArr[5]
    pyjson['G'] = cleanArr[6]
    pyjson['H'] = cleanArr[7]
    pyjson['I'] = cleanArr[8]
    pyjson['J'] = cleanArr[9]
    pyjson['K'] = cleanArr[10]
    pyjson['L'] = cleanArr[11]

    pyjson['R'] = cleanArr[12]
    pyjson['S'] = cleanArr[13]
    pyjson['T'] = cleanArr[14]
    pyjson['U'] = cleanArr[15]
    pyjson['V'] = cleanArr[16]
    pyjson['W'] = cleanArr[17]

    data = arduino.readline()
    data = arduino.readline()
    data = arduino.readline()
    data = arduino.readline()
    return pyjson

# print(sensors())
# print("\n")
# print(triad())