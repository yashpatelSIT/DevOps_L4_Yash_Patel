from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def hello():
    os.makedirs("/app/data", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("/app/data/log.txt", "a") as file:
        file.write(f"Hello, Docker! - {timestamp}\n")

    return "Hello, Docker! Data has been saved."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)