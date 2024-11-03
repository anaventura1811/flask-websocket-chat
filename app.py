from flask import Flask, render_template
from flask import request, session, redirect, url_for, Response
from flask_socketio import SocketIO, leave_room, join_room, send
from dotenv import load_dotenv
import os
from helpers import generate_unique_code
from datetime import datetime
from typing import Dict


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

socketio = SocketIO(app)


rooms = {}


@app.route('/', methods=['GET', 'POST'])
def home() -> (str | Response):
    session.clear()
    if request.method == 'POST':
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", "False")
        create = request.form.get("create", "False")

        if not name:
            return render_template(
                'home.html',
                error="Por favor, digite um username",
                code=code,
                name=name,
                )
        if join != "False" and not code:
            return render_template(
                'home.html',
                error="Por favor, digite o código da sala",
                code=code,
                name=name,
                )
        room = code
        if create != "False":
            room = generate_unique_code(length=4, rooms=rooms)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("home.html",
                                   error="Sala não existe!",
                                   code=code,
                                   name=name)
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))
    return render_template('home.html')


@app.route('/room', methods=['GET'])
def room() -> (str | Response):
    room = session.get("room")
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("home"))
    return render_template('room.html',
                           room=room,
                           messages=rooms[room]["messages"])


@socketio.on("message")
def message(data: Dict) -> None:
    room = session.get("room")
    if room not in rooms:
        return
    content = {
        "name": session.get("name"),
        "message": data["data"],
        "time": str(datetime.now())
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")


@socketio.on('connect')
def connect() -> None:
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    join_room(room)
    send({"name": name,
          "message": "has entered the room",
          "time": str(datetime.now())}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")


@socketio.on('disconnect')
def disconnect() -> None:
    room = session.get("room")
    name = session.get("name")

    leave_room(room)
    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")
    print('Client has disconnect from sockets')


if __name__ == '__main__':
    socketio.run(app, debug=True)
