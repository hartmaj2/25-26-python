# simple code for a server which can be used to share files via local network

# add attribute accept=".py" to accept only files with .py file extension

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        file.save(file.filename)
        return "Uploaded"

    return '''
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button>Upload</button>
    </form>
    '''

app.run(host="0.0.0.0", port=80) # the default port is 80