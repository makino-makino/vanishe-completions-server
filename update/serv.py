from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import urllib.parse


from models import session, Word

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/update", methods=['GET'])
@cross_origin()
def update():
    first = request.args.get('first', default=0, type=int)

    words = session.query(Word).\
        filter(Word._id >= first).\
        all()
    
    result = []
    for word in words:
        result.append({
            'id': urllib.parse.quote(str(word._id)),
            'yomi': urllib.parse.quote(word.yomi),
            'kaki': urllib.parse.quote(word.kaki)
        })
    
    return jsonify(result)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

# /root/go/bin/ojichat
