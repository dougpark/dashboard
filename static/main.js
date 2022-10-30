// https://flask-socketio.readthedocs.io/en/latest/intro.html

function init() {
    var socket = io()
    var loggerElement = document.getElementById('logger')
    var dataElement = document.createElement('pre')
    dataElement.innerHTML = "Started"
    loggerElement.appendChild(dataElement)

    console.log('sending first connect/one to server:')
    socket.emit('one', {data: 'connect/one'})

    console.log('sending mirror/one to server:')
    socket.emit('mirror', {data: 'First mirror data sent from client'})

    console.log('sending mirror/two to server:')
    socket.emit('mirror', {data: 'Second mirror data sent from client'})

    socket.on('mirrorResp', function (payload) {
        console.log('mirror response from server:')
        console.log(payload)
        var dataElement = document.createElement('pre')
        dataElement.innerHTML = payload.data
        loggerElement.appendChild(dataElement)
    })

    socket.on('oneResp', function (payload) {
        console.log('one response from server:')
        console.log(payload)
        var dataElement = document.createElement('pre')
        dataElement.innerHTML = payload.data
        loggerElement.appendChild(dataElement)
    })

    socket.on('connectResp', function (payload) {
        console.log('connect response from server:')
        console.log(payload)
        var dataElement = document.createElement('pre')
        dataElement.innerHTML = payload.data
        loggerElement.appendChild(dataElement)
    })

}

$( window ).on( "load", function() {
  init()
})
