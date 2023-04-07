import os
class Config:
    DEBUG = True
    STEAM_API_KEY = os.environ.get("STEAM_API_KEY")
    FIREBASE_CRED_CERTIFITACE = "gameder-1163d-39552ceb875d.json"

