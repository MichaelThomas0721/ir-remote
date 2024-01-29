from flask import Flask, render_template, Response, send_from_directory
from database import SetupDatabase, GetData, InsertData
import sqlite3
import json
import time
import random

app = Flask(__name__)
SetupDatabase()
print(GetData("pending"))
InsertData("pending", "SIUFDSIUF")

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

@app.route("/<path:path>")
def home(path):
    print(path)
    return send_from_directory('client/public', path)

def generate():
    data = GetData("pending")
    data = json.dumps(data)
    return data

@app.route('/stream')
def stream():
    res = generate()
    return Response(res, mimetype='text/plain')

@app.route('/start_recording')
def start_recording():
    # This is where the ir receiver function would be called
    print("START RECORDING")
    return Response("bruv", mimetype='text/plain');

# Path for all the static files (compiled JS/CSS, etc.)
# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory('client/public', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5173)