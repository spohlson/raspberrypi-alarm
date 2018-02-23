from flask import Flask, jsonify, request
from threading import Thread
import time
from datetime import datetime
from tkinter import messagebox

app = Flask(__name__)

# class RunAlarm(Thread):
#     
#     def __init__(self, queue):
#         Thread.__init__(self)
#         self.queue = queue
#     
#     def run(self):
#         while True:
#             datetime = self.queue.get()
#             set_alarm(datetime)
#             self.queue.task_done()

@app.route('/')
def hello():
    """Simple example of an API endpoint"""
    return jsonify({'message': 'ohai'})


@app.route('/hello/<string:name>')
def hello_name(name):
    """Simple example using an URL parameter"""
    return jsonify({'message': 'ohai {}'.format(name)})

@app.route('/alarm', methods = ['POST'])
def set_alarm_api():
    """ time format should be: yyyy-MM-dd’T’HH:mm """
    date_text = request.json['time']
    message = request.json['message']
    
    alarm_time = validate_datetime(date_text)
    set_alarm(alarm_time, message)
    
    return jsonify('Success!')

def set_alarm(alarmTime:datetime, message:str = 'Alert Alert!'):
    print('alarm time - {}'.format(alarmTime))
    print('now - {}'.format(datetime.now()))
    time.sleep((alarmTime - datetime.now()).total_seconds())
    messagebox.showinfo('Alarm', message)


def validate_datetime(date_text:str) -> datetime:
    try:
        formatted_time = datetime.strptime(date_text, '%Y-%m-%dT%H:%M')
        print('Formatted Time: {}'.format(formatted_time))
        return formatted_time
    except ValueError:
        raise ValueError('Incorrect data format, should be yyyy-MM-dd’T’HH:mm')

if __name__ == '__main__':
#     import sys;sys.path.append(r'/Users/shawnpohlson/.p2/pool/plugins/org.python.pydev_6.2.0.201711281614/pysrc')
#     import pydevd;pydevd.settrace()
    port = 5000 #the custom port you want
    app.run(host='0.0.0.0', port=port)
