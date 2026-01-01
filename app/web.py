from flask import Flask, render_template, request, send_from_directory
from file_handler import secure_store, secure_retrieve
from crypto.rsa_utils import generate_keys
import os

app = Flask(__name__)
private_key, public_key = generate_keys()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        path = os.path.join("storage", file.filename)
        file.save(path)
        secure_store(path, public_key)
    return render_template("index.html")

@app.route("/download/<filename>")
def download(filename):
    secure_retrieve(filename, private_key)
    return send_from_directory("storage", filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
