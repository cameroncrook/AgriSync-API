from flask import Flask
from flask_cors import CORS

# blueprints
from api.v1.apiAgriSync import apiAgriSync
from api.v1.apiHarvests import apiHarvests

app = Flask(__name__)

CORS(app)

# register blueprints
app.register_blueprint(apiAgriSync)
app.register_blueprint(apiHarvests)

@app.route('/')
def index():
    return '<h1>AgriSync API</h1>'