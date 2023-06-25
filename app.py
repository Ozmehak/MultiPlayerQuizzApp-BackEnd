from flask import Flask
from flask_socketio import SocketIO
import os

SECRET_KEY = os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)


@app.route('/')
def api_index():
    return 'Welcome to the API for our Multiplayer Quizz App!'
