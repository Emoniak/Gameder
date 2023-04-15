from flask import Flask, request, jsonify
from firebase_admin import firestore
import requests

from api import app
app.config.from_object('config.Config')
db = firestore.client()

@app.route('/steam/UpdateGame', methods=['POST'])
def SetGameToFirestore():
    body = request.get_json()
    steamuserid = body['steamid']
    userid = body['userid']

    games = ListGame(steamuserid)
    print (games)
    db.collection("production").document(userid).collection("steamlib").document("games").set(games)
    
    response = {'message': 'Données publiées avec succès'}

    return jsonify(response)

@app.route('/steam/ListGame/<steamuserid>', methods=['GET'])
def ListGame(steamuserid):
    param = {
        "key" : app.config['STEAM_API_KEY'],
        "steamid" : steamuserid,
        "format": "json"
    }
    game_list = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001",params=param).json()["response"]["games"]

    detail_game_list = []
    error_list = []

    for game in game_list:
        query = {"appids":game["appid"]}
        try:
            detail_game_list.append(requests.get("https://store.steampowered.com/api/appdetails",params=query).json())
        except Exception as e:
            error_list.append(e)
        
    return jsonify(detail_game_list)