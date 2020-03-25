from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import hashlib, subprocess
import urllib.parse

TIMEOUT = 10

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/echo-sd", methods=['GET'])
@cross_origin()
def echo_sd():
    msg = request.args.get('msg')

    process = subprocess.run(
        ['/script/echo-sd', msg],
        capture_output=True,
        encoding='utf-8',
        timeout=TIMEOUT)

    result = process.stdout
    result = urllib.parse.quote(result)

    return jsonify({"result": result})

@app.route("/ojichat", methods=['GET'])
@cross_origin()
def ojichat():
    msg = request.args.get('msg')

    process = subprocess.run(
        ['/root/go/bin/ojichat', msg],
        capture_output=True,
        encoding='utf-8',
        timeout=TIMEOUT)

    result = process.stdout
    result = urllib.parse.quote(result)

    return jsonify({"result": result})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# /root/go/bin/ojichat
