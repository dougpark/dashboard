// https://flask-socketio.readthedocs.io/en/latest/intro.html

var socket = io()

function init() {
    var loggerElement = document.getElementById('logger')
    var dataElement = document.createElement('pre')
    loggerElement.innerHTML = ''
    dataElement.innerHTML = "Server Started"
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
  
    socket.on('refreshResp', function (payload) {
      console.log('refresh response from server:')
      console.log(payload)
      // var loggerElement = document.getElementById('logger')
      var dataElement = document.getElementById('refreshVal')
      dataElement.innerHTML = payload.data
      // loggerElement.appendChild(dataElement)
  })

}

function refresh() {
  console.log('sending refresh to server:')
  socket.emit('refresh', {data: 'Refresh sent from client'})
}

function openTab(evt, tabName) {
  var i, tabs, tablinks;
  tabs = document.getElementsByClassName("tab");
  for (i = 0; i < tabs.length; i++) {
      tabs[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" w3-border-red", " w3-border-blue");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " w3-border-red";
}


$(window).on("load", function () {

  $("#refresh").click(function (e) {
    var idClicked = e.target.id;
    console.log(idClicked)
  
    refresh()
  
  });
  
  console.log('window loaded')
    init()
})
