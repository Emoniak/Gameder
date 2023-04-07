from flask import jsonify

from api import app

@app.route('/steam', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})
