from flask import Flask, request, jsonify, render_template, Response, send_from_directory
from database import SetupDatabase, GetData, InsertSequenceData, RunSql, SaveSequence, GetPendingSequence, GetAllSequences
import sqlite3
import json
import time
import random

app = Flask(__name__)
SetupDatabase()
print(GetData("pending"))
# InsertSequenceData("pending", "SIUFDSIUF")

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

@app.route('/save_sequence', methods = ['POST'])
def save_sequence():
    data = request.get_json()
    if request.method == 'POST':
        sequence_id = data.get('sequence_id')
        name = data.get('name')
        sequences = GetPendingSequence(data.get('sequence_id'))
        SaveSequence(sequences[0], name)
        return jsonify({'status': '200'})



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5173)