from flask import Flask, request, jsonify

import hashlib, subprocess
import urllib.parse

TIMEOUT = 10

app = Flask(__name__)

@app.route("/echo-sd", methods=['GET'])
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
