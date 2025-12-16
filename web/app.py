from flask import Flask, render_template, request
import subprocess, os

app = Flask(__name__)
UPLOAD = "uploads"
os.makedirs(UPLOAD, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""

    if request.method == "POST":
        if "zip" not in request.files:
            return "No file uploaded"

        file = request.files["zip"]

        if file.filename == "":
            return "No file selected"

        path = os.path.join(UPLOAD, file.filename)
        file.save(path)

        checker = subprocess.run(
            ["python3", "../checker/code_checker.py"],
            input=path,
            text=True,
            capture_output=True
        )

        simulator = subprocess.run(
            ["python3", "../simulator/run_simulation.py"],
            capture_output=True,
            text=True
        )

        output = checker.stdout + "\n" + simulator.stdout

    return render_template("index.html", out=output)

if __name__ == "__main__":
    app.run(debug=True)

