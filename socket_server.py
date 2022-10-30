from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
# https://flask-socketio.readthedocs.io/en/latest/intro.html

app = Flask(__name__)
app.config['SECRET_KEY'] = 'justasecretkeythatishouldputhere'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    print('api called')
    query = dict(request.args)
    socketio.emit('log', dict(data=str(query)), broadcast=True)
    return jsonify(dict(success=True, message='Received'))

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