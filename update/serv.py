from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/update", methods=['GET'])
@cross_origin()
def update():
    first = request.args.get('fitst')
    result = 'hello'
    return jsonify({"result": result})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

# /root/go/bin/ojichat
