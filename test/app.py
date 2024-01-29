from flask import Flask, render_template, Response
from databaseSetup import SetupDatabase, GetData, InsertData
import sqlite3
import time

app = Flask(__name__)
SetupDatabase()
print(GetData())
InsertData("SIUFDSIUF")

@app.route('/')
def index():
    return render_template('index.html')

def generate():
    with open('job.log') as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            yield line
    time.sleep(1)

@app.route('/stream')
def stream():
    res = generate()
    print("RES", res)
    return Response(res, mimetype='text/plain')

if __name__ == "__main__":
    app.run()
