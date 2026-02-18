from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Launch date: 19-Feb-2026 at 12:00 PM UTC
LAUNCH_DATE = datetime(2026, 2, 19, 12, 0, 0)

@app.route("/")
def home():
    return render_template("index.html", launch_date=LAUNCH_DATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
