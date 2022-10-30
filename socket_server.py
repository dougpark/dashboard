from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
# https://flask-socketio.readthedocs.io/en/latest/intro.html
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'justasecretkeythatishouldputhere'
socketio = SocketIO(app)
refreshVal = 0

@app.route('/')
def index():
    return render_template('index.html',date=datetime.now())

@app.route('/api')
def api():
    print('api called')
    query = dict(request.args)
    socketio.emit('log', dict(data=str(query)), broadcast=True)
    return jsonify(dict(success=True, message='Received'))

@socketio.on('refresh')
def refreshFunc(data):
    global refreshVal
    print('refresh called')
    refreshVal = refreshVal + 1
    payload = dict(data=refreshVal)
    emit('refreshResp', payload, broadcast=True)

@socketio.on('one')
def one(data):
    print('one called')
    print(request.sid)
    payload = dict(data='This response is from one')
    emit('oneResp', payload)

@socketio.on('mirror')
def mirror(data):
    print('mirror called')
    print(data)
    payload = data
    emit('mirrorResp', payload)

@socketio.on('connect')
def on_connect():
    print('connected called')
    payload = dict(data='Connection ack from server')
    emit('connectResp', payload)

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', port=5000)