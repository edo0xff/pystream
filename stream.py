# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import cv2
from flask import Flask
from flask import render_template
from flask import Response

cap = cv2.VideoCapture(0)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        ret, frame = cap.read()
        frame = cv2.imencode('.jpg', frame)[1].tostring()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    ip = raw_input('Ip a utilizar: ')
    app.run(host=ip, processes=3)