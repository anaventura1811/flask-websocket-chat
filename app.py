from flask import Flask, render_template, request
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os
from helpers import generate_unique_code


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

socketio = SocketIO(app)


rooms = {}
session = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template(
                'home.html',
                error="Por favor, digite um username",
                code=code,
                name=name,
                )
        if join and not code:
            return render_template(
                'home.html',
                error="Por favor, digite o código da sala",
                code=code,
                name=name,
                )
        room = code
        if create:
            room = generate_unique_code(length=4, rooms=rooms)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("home.html",
                                   error="Sala não existe!",
                                   code=code,
                                   name=name)
        session["room"] = room
        session["name"] = name
    return render_template('home.html')


@app.route('/chat', methods=['GET'])
def get_page():
    return render_template('index.html')


@socketio.on('connect')
def connect():
    print('>>>> Client is connected!!')


@socketio.on('disconnect')
def disconnect():
    print('Client has disconnect from sockets')


if __name__ == '__main__':
    socketio.run(app, debug=True)
