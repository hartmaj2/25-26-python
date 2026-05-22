from flask import Flask, send_file

app = Flask(__name__)

FILES = ["text.txt", "text.png", "text.mp3", "text.docx"]


@app.route("/")
def index():
    links = ""

    for filename in FILES:
        links += f'<p><a href="/download/{filename}">{filename}</a></p>'

    return f"""
    <h1>Download files</h1>
    {links}
    """


@app.route("/download/<filename>")
def download(filename):
    if filename not in FILES:
        return "File not allowed", 403

    return send_file(filename, as_attachment=True)


app.run(host="0.0.0.0", port=80)