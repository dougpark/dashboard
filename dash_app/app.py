from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
# https://flask-socketio.readthedocs.io/en/latest/intro.html
from datetime import datetime
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'justasecretkeythatishouldputhere'
socketio = SocketIO(app)
refreshVal = 0
msgStatus = False
msg = 'On Air'

# logging configuration
# debug, info, warning, error, critical
logging.basicConfig(filename='./instance/server.log',
                    level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('Started')
logging.info('running socket_server.py')

@app.route('/')
def index():
    return render_template('index.html',date=datetime.now())

@app.route('/api')
def api():
    logging.info('api called')
    query = dict(request.args)
    socketio.emit('log', dict(data=str(query)), broadcast=True)
    return jsonify(dict(success=True, message='Received'))

@app.route('/onair')
def onair():
    logging.info('onair called')
    query = dict(request.args)
    # socketio.emit('log', dict(data=str(query)), broadcast=True)
    global msgStatus
    msgStatus = True
    payload = dict(data='ok', messageStatus=msgStatus,message=msg)
    socketio.emit('msgStatus', payload, broadcast=True)
    return render_template('index.html',date=datetime.now())


@socketio.on('refresh')
def refreshFunc(data):
    global refreshVal
    logging.info('refresh called')
    refreshVal = refreshVal + 1
    payload = dict(data=refreshVal, messageStatus=msgStatus, message=msg)
    emit('refreshResp', payload, broadcast=True)

@socketio.on('getrefresh')
def getrefreshFunc(data):
    logging.info('getrefresh called')
    payload = dict(data=refreshVal, messageStatus=msgStatus, message=msg)
    emit('refreshResp', payload, broadcast=True)

@socketio.on('showmsg')
def showMsg(data):
    global msgStatus
    logging.info('showMsg called')
    msgStatus = True
    payload = dict(data='ok', messageStatus=msgStatus,message=msg)
    emit('msgStatus', payload, broadcast=True)

@socketio.on('hidemsg')
def hideMsg(data):
    global msgStatus
    logging.info('hideMsg called')
    msgStatus = False
    payload = dict(data='ok', messageStatus=msgStatus, message=msg)
    emit('msgStatus', payload, broadcast=True)

@socketio.on('getmsg')
def getMsg(data):
    logging.info('getMsg called')
    payload = dict(data='ok', messageStatus=msgStatus, message=msg)
    emit('msgStatus', payload, broadcast=True)

@socketio.on('one')
def one(data):
    logging.info('one called')
    logging.info(request.sid)
    payload = dict(data='This response is from one')
    emit('oneResp', payload)

@socketio.on('mirror')
def mirror(data):
    logging.info('mirror called')
    logging.info(data)
    payload = data
    emit('mirrorResp', payload)

@socketio.on('connect')
def on_connect():
    logging.info('connected called')
    payload = dict(data='Connection ack from server')
    emit('connectResp', payload)

if __name__ == '__main__':
    # allow_unsafe_werkzeug=True - allows flask to run in docker container as production. Not safe.
    socketio.run(app,allow_unsafe_werkzeug=True,host='0.0.0.0', port=5000)