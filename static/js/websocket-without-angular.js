var ws = new WebSocket("ws://" + document.location.host + "/websocket");
ws.onopen = function() {
    ws.send("hello");
};
ws.onmessage = function (evt) {
    var
        data = JSON.parse(evt.data);
    alert(data);
};
ws.onclose = function (evt) {
    ws.send('close');
};

function reconnect_if_needed() {
    if (ws.readyState == 0 || ws.readyState == 1) {
        return;
    } else {
        ws = new WebSocket("ws://" + document.location.host + "/websocket");
    }
};

window.onbeforeunload = function() {
    ws.send('close');
    ws.onclose = function () {}; // disable onclose handler first
    ws.close()
};

function handle_logout(e) {
    ws.send('close');
    ws.onclose = function () {}; // disable onclose handler first
    ws.close();

    document.location = 'logout';

    return false;
};
