from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return "working webserver"

# 2020-05-05 21:09:13.663307,192.168.1.151,sysName.0,raspberrypi
@app.route('/api/host/<string:host>', methods=['GET'])
def get_host(host):
    output = []
    with open('results.csv') as results:
        resultscsv = csv.reader(results)
        for row in resultscsv:
            if row[1] == host:
                output.append({'hostname': row[1],
                               'timestamp': row[0],
                               'mib': row[2],
                               'output': row[3]},)
        return jsonify(output)

app.run(debug=True)