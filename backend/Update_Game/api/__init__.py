from flask import Flask
import firebase_admin
from firebase_admin import credentials

app = Flask(__name__)

app.config.from_object('config.Config')
cred = credentials.Certificate(app.config['FIREBASE_CRED_CERTIFITACE'])
firebase_admin.initialize_app(cred)

from api.endpoints import DebugEndpoint
from api.endpoints import Steam
