import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio)

messages = []


@sio.event
def connect(sid, environ):
    print("Connected to python server")
    print('connect ', sid)
    sio.emit("getMessages", data=messages)


@sio.event
def disconnect(sid):
    print("Disconnected to python server")
    print('disconnect ', sid)


# @sio.on("salutations")
# def salutations(sid, data):
#     print(f"Received data : {data}")
#     for item in data:
#         print(f"{type(item)}\n")


@sio.on("sendMessage")
def send_message(sid, message):
    print(f"Receive message : {message} and Sid : ${sid}")
    messages.append(message)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
