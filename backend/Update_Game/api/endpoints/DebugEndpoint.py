import sys
from flask import jsonify
import json

from api import app
app.config.from_object('config.Config')

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

@app.route('/config', methods=['GET'])
def steamkey():
    with open(app.config['FIREBASE_CRED_CERTIFITACE']) as f:
        firebaseConfig = json.load(f)
    config = {
        'steamkey' :  app.config['STEAM_API_KEY'],
        'firebaseCertifPath' : app.config['FIREBASE_CRED_CERTIFITACE'],
        'firebaseCertif' : firebaseConfig
    }

    return jsonify(config)

@app.route('/', methods=['GET'])
def index():
    # Obtenir la version de Python
    python_version = sys.version

    # Retourner les informations sous forme de JSON
    info = {
        'python_version': python_version
    }
    return jsonify(info)