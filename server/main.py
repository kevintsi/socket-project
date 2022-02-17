import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print("Connected to python server")
    print('connect ', sid)
    sio.emit("greetings", data=(
        ["rdfdfd20", 10, {"test": "foobar"}], 230, "test"
    ))


@sio.event
def disconnect(sid):
    print("Disconnected to python server")
    print('disconnect ', sid)


@sio.on("salutations")
def salutations(sid, data):
    print(f"Received data : {data}")
    for item in data:
        print(f"{type(item)}\n")


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
