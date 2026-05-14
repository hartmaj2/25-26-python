from flask import Flask, request, redirect, make_response
from html import escape

app = Flask(__name__)
messages = []

@app.route("/", methods=["GET", "POST"])
def chat():
    nickname = request.cookies.get("nickname", "")

    if request.method == "POST":
        if "nickname" in request.form:
            response = redirect("/")
            response.set_cookie("nickname", request.form["nickname"])
            return response

        text = request.form["text"]
        messages.append(f"{nickname or request.remote_addr}: {text}")
        return redirect("/")

    return f"""
    <h1>Class Chat</h1>

    <h2>Set nickname</h2>
    <form method="post">
        <input name="nickname" value="{escape(nickname)}" placeholder="Nickname">
        <button>Save nickname</button>
    </form>

    <h2>Send message</h2>
    <form method="post">
        <input name="text" placeholder="Message">
        <button>Send</button>
    </form>

    <hr>
    {"<br>".join(escape(m) for m in messages)}
    """

app.run(host="0.0.0.0", port=80)