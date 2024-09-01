from app import app
import json
# import serial
# from cameras import gen_frames0
# , gen_frames1, gen_frames2, gen_frames3, gen_frames4, gen_frames5
from flask import Flask, Response
from flask import render_template
from controls import wheels
# from science import sensor
# from controls import get_plot
# #imuData
# from arm import arm
# from graphs import getGraph


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/controls')
def controls():
    return render_template('controls.html')


@app.route('/get-map')
def get_map():
    return get_plot()
    # map = your_function()
    # return map
@app.route('/get-graph')
def get_graph():
    return getGraph()

@app.route('/get-imu')
def get_imu():
    return imuData()


@app.route('/get-dictionary')
def get_dictionary():
    dictionary = sensor()
    return dictionary


@app.route('/science')
def science():
    return render_template('science.html')


@app.route('/camera')
def cam():
    return render_template('cameras.html')


@app.route('/video_feed0')
def video_feed0():
    return Response(gen_frames0(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed1')
def video_feed1():
    return Response(gen_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed2')
def video_feed2():
    return Response(gen_frames2(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed3')
def video_feed3():
    return Response(gen_frames3(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed4')
def video_feed4():
    return Response(gen_frames4(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed5')
def video_feed5():
    return Response(gen_frames5(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/forward')
def forward():
    while (True):
        return Response(wheels('F'))


@app.route('/backward')
def backward():
    while (True):
        return Response(wheels('B'))


@app.route('/left')
def left():
    while (True):
        return Response(wheels('L'))


@app.route('/right')
def right():
    while (True):
        return Response(wheels('R'))


@app.route('/stop')
def stop():
    while (True):
        return Response(wheels('S'))


@app.route('/partialL')
def partialLeft():
    while (True):
        return Response(wheels('x'))


@app.route('/partialR')
def partialRight():
    while (True):
        return Response(wheels('y'))


@app.route('/m1-forward')
def m1f():
    while (True):
        return Response(arm('A'))


@app.route('/m1-backward')
def m1b():
    while (True):
        return Response(arm('B'))


@app.route('/m2-forward')
def m2f():
    while (True):
        return Response(arm('C'))


@app.route('/m2-backward')
def m2b():
    while (True):
        return Response(arm('D'))


@app.route('/m3-forward')
def m3f():
    while (True):
        return Response(arm('E'))


@app.route('/m3-backward')
def m3b():
    while (True):
        return Response(arm('F'))


@app.route('/m4-forward')
def m4f():
    while (True):
        return Response(arm('G'))


@app.route('/m4-backward')
def m4b():
    while (True):
        return Response(arm('H'))


@app.route('/m5-forward')
def m5f():
    while (True):
        return Response(arm('I'))


@app.route('/m5-backward')
def m5b():
    while (True):
        return Response(arm('J'))


@app.route('/m6-forward')
def m6f():
    while (True):
        return Response(arm('K'))


@app.route('/m6-backward')
def m6b():
    while (True):
        return Response(arm('L'))


@app.route('/m-stop')
def mstop():
    while (True):
        return Response(arm('X'))

# arduino_port = 'COM5'  # Update with your Arduino port
# baud_rate = 115200  # Must match the Arduino baud rate
# ser = serial.Serial(arduino_port, baud_rate)

# data_list = [0]
# x_values = [380, 450, 485, 500, 565, 590, 625, 750]

# def read_arduino_data():
#     while True:
#         if ser.in_waiting > 0:
#             arduino_data = ser.readline().decode().rstrip().replace('\t', ',')
#             arduino_data.split(',')
#             data_list.pop()
#             data_list.append(arduino_data)
#             y_values = [int(value) for value in data_list[0].split(',')]
#             data = {'x': x_values, 'y': y_values}
#             print(data)

@app.route('/get_data')
def get_data():
    y_values = [int(value) for value in data_list[0].split(',')]
    data = {'x': x_values, 'y': y_values}
    return json.dumps(data)


@app.route('/controller')
def control_arm():
    return Response(controller())
