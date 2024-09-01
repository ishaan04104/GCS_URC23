# Import necessary libraries
from flask import Flask, Response, url_for
import threading
app = Flask(__name__)

# from science import *
# from controls import *
from routes import *
# from arm import *
# from graphs import *

if __name__ == '__main__':

    # arduino_thread = threading.Thread(target=read_arduino_data)
    # arduino_thread.daemon = True
    # arduino_thread.start()
    app.run(debug=True)
    
