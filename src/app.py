from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        os.makedirs("uploads", exist_ok=True)
        file.save(os.path.join("uploads", file.filename))
        return f"Uploaded: {file.filename}"
    return "No file uploaded"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
