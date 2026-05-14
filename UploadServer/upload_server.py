# simple code for a server which can be used to share files via local network

from flask import Flask, request

app = Flask(__name__)

only_python = '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".py">
        <button>Upload</button>
    </form>
    '''

accept_all = '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button>Upload</button>
    </form>
    '''

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        file.save(file.filename)
        return "Uploaded"

    return accept_all

app.run(host="0.0.0.0", port=80) # the default port is 80