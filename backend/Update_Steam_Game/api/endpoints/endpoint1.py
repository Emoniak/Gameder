from flask import jsonify

from api import app

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})
