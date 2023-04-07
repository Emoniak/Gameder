from flask import Flask, request, jsonify
from firebase_admin import firestore

from api import app

db = firestore.client()

@app.route('/steam/UpdateGame', methods=['POST'])
def SetGameToFirestore():
    body = request.get_json()
    steamuserid = body['steamid']
    userid = body['userid']

    steamgameid = "1"
    games = {
        u"name": u"Jeux de test"
    }

    db.collection("production").document(userid).collection("steamlib").document(steamgameid).set(games)
    
    response = {'message': 'Données publiées avec succès'}

    return jsonify(response)
