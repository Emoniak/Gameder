from flask import Flask

app = Flask(__name__)

from api.endpoints import DebugEndpoint
from api.endpoints import Steam
