from flask import Flask, render_template
from flask_socketio import SocketIO
import os

SECRET_KEY = os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)