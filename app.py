from flask import Flask
from flask_socketio import SocketIO, send, join_room, leave_room
import os
import utils

SECRET_KEY = os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@app.route('/' , methods=['GET'])
def api_index():
    return 'Welcome to the API for our Multiplayer Quizz App!'



@socketio.on('create_room')
def handle_create_room(data):
    '''Create a new room and return the room code'''
    room_code = utils.generate_room_code()
    join_room(room_code)
    socketio.emit('room_created', room_code, room=room_code)
    print('Room created:', room_code)
    return room_code


@socketio.on('join')
def on_join(data):
    '''Join a room with the given room code, username and 
    send a message to the room that a user has entered'''
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)


@socketio.on('leave')
def on_leave(data):
    '''Leave a room with the given room code, username and
    send a message to the room that a user has left'''
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)


@socketio.on('send_message')
def handle_send_message(data):
    '''Send a message to the room with the given room code'''
    room = data['room']
    message = data['message']
    send(message, to=room)  



