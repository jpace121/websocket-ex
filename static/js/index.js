// js file for index.html

var socket = new WebSocket("ws://localhost:8888/ws");

socket.onopen = function (event) {
    socket.send("test");
    console.log("HI");
}
