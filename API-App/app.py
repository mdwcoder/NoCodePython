from flask import Flask, request, jsonify
from flask_cors import CORS
import os

LocalIp = os.getenv('IP')
Frontend_Port = os.getenv('FrontEndPort')
Backend_Port = os.getenv('BackEndPort')

app = Flask(__name__)
CORS(
    app,
    supports_credentials=True,
    methods=["GET", "POST", "DELETE", "OPTIONS"],
    headers=["Content-Type", "X-Requested-With",
             "X-CSRFToken", "Authorization"],
    origins=[f"http://localhost:{Frontend_Port}",
             f"{LocalIp}{Frontend_Port}",
             f"{LocalIp}",
             ]
)

@app.route('/API/translate', Methods=["GET"])
def translate_fn():
    data = request.json
    Natulal_Lenguaje_Code = data.get('NaturalLenguajeCode')
    pass

    return jsonify({'':''})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(Backend_Port))
