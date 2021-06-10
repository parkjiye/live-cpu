from flask import Flask, jsonify, request, render_template, Response
from datetime import datetime
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	return render_template('index.html', value='get')

@app.route('/main')
def main():
	return render_template('main.html', value='get')

@app.route('/test')
def test_world():
	return 'Test, World!'

import psutil

@app.route('/cpu_feed')
def cpu_feed():
    def generate():
        #print(str(psutil.cpu_percent()))
        yield str(psutil.cpu_percent())
    return Response(generate(), mimetype='text')

@app.route('/time_feed')
def time_feed():
    def generate():
        yield datetime.now().strftime("%Y.%m.%d|%H:%M:%S")  # return also will work
    return Response(generate(), mimetype='text')

import json
from time import time
from flask import make_response

@app.route('/live-data')
def live_data():
    cpu=psutil.cpu_percent()
    data=[time()*1000, cpu]
    response=make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=18092)