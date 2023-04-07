import subprocess
import sys
from flask import jsonify

from api import app
app.config.from_object('config.Config')

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

@app.route('/steamkey', methods=['GET'])
def steamkey():
    return jsonify({'key': app.config['STEAM_API_KEY']})

@app.route('/', methods=['GET'])
def index():
    # Obtenir la version de Python
    python_version = sys.version

    # Retourner les informations sous forme de JSON
    info = {
        'python_version': python_version
    }
    return jsonify(info)