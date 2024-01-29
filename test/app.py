from flask import Flask, render_template, Response
from database import SetupDatabase, GetData, InsertData
import sqlite3
import json
import time

app = Flask(__name__)
SetupDatabase()
print(GetData("pending"))
InsertData("pending", "SIUFDSIUF")

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == "__main__":
    app.run()
