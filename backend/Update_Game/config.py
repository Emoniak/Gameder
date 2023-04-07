import os
class Config:
    DEBUG = True
    STEAM_API_KEY = os.environ.get("STEAM_API_KEY")

