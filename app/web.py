from flask import Flask, render_template, request, send_file
from app.file_handler import secure_store, secure_retrieve
from crypto.rsa_utils import generate_keys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORAGE_DIR = os.path.join(BASE_DIR, "storage")

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"),
                    static_folder=os.path.join(BASE_DIR, "static"))

private_key, public_key = generate_keys()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        path = os.path.join(STORAGE_DIR, file.filename)
        file.save(path)
        secure_store(path, public_key)
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download_file():
    filename = request.form["filename"]
    secure_retrieve(filename, private_key)

    file_path = os.path.join(STORAGE_DIR, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
