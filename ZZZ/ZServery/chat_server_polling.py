from flask import Flask, request, redirect

app = Flask(__name__)
messages = []

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        ip = request.remote_addr
        text = request.form["text"]
        messages.append(f"{ip}: {text}")
        return redirect("/")

    return """
    <h1>Class Chat</h1>

    <form method="post">
        <input name="text" placeholder="Message">
        <button>Send</button>
    </form>

    <hr>

    <div id="messages"></div>

    <script>
        async function updateMessages() {
            let response = await fetch("/messages");
            let html = await response.text();
            document.getElementById("messages").innerHTML = html;
        }

        setInterval(updateMessages, 1000);
    </script>
    """

@app.route("/messages")
def get_messages():
    return "<br>".join(messages)

app.run(host="0.0.0.0", port=80)