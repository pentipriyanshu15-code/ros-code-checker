from flask import Flask, request, render_template_string
import subprocess
import os

app = Flask(__name__)

HTML = """
<h2>ROS Code Checker & Simulation</h2>

<form method="post" enctype="multipart/form-data">
  <input type="file" name="zipfile" required>
  <input type="submit" value="Run Checker & Simulation">
</form>

<h3>Output:</h3>
<pre>{{ output }}</pre>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        file = request.files["zipfile"]
        zip_path = os.path.join("/tmp", file.filename)
        file.save(zip_path)

        # Run code checker
        checker = subprocess.run(
            ["python3", "../checker/code_checker.py"],
            input=zip_path + "\n",
            text=True,
            capture_output=True
        )

        # Run simulation
        simulation = subprocess.run(
            ["python3", "../simulator/run_simulation.py"],
            text=True,
            capture_output=True
        )

        output = checker.stdout + "\n--- Simulation Output ---\n" + simulation.stdout

    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5010, debug=False)

