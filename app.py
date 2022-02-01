#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response, url_for
from flask_bootstrap import Bootstrap
from camera import VideoCamera


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    TITLE = 'DLearning EmoRecognizer'
    return render_template('index.html', TITLE=TITLE)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5000")


