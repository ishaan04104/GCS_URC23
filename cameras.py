import cv2

port1=1
# port1=1
# port2=2
# port3=3
# port4=4
# port5=5

camera0 =cv2.VideoCapture(port1)
# camera1 =cv2.VideoCapture(port1)
# camera2 =cv2.VideoCapture(port2)
# camera3 =cv2.VideoCapture(port3)
# camera4 =cv2.VideoCapture(port4)
# camera5 =cv2.VideoCapture(port5)

# '''
# for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
# for local webcam use cv2.VideoCapture(0)
# '''
# def gen_frames0():
#     while True:
#         success, frame = camera0.read() # read the camera frame
        
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'b'Content-Type: imimg src="{{ url_for('video_feed') }}">age/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
# img src="{{ url_for('video_feed') }}">
# def gen_frames0():
#     while True:
#         success, frame = camera0.read() # read the camera frame

#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

# def gen_frames2():
#     while True:
#         success, frame = camera2.read() # read the camera frame

#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

# def gen_frames3():
#     while True:
#         success, frame = camera3.read() # read the camera frame

#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

# def gen_frames4():
#     while True:
#         success, frame = camera4.read() # read the camera frame

#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

# def gen_frames5():
#     while True:
#         success, frame = camera5.read() # read the camera frame

#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
