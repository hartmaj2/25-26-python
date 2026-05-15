# Run `ipconfig getifaddr en0` to find out LAN address

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Lock

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"

socketio = SocketIO(app, cors_allowed_origins="*")

cookies = 0
cookies_lock = Lock()


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def handle_connect():
    emit("state", {"cookies": cookies})


@socketio.on("click")
def handle_click():
    global cookies

    with cookies_lock:
        cookies += 1
        current_cookies = cookies

    socketio.emit("state", {"cookies": current_cookies})


@socketio.on("reset")
def handle_reset():
    global cookies

    with cookies_lock:
        cookies = 0

    socketio.emit("state", {"cookies": cookies})


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80, debug=True)