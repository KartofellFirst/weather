from flask import Flask, request
import json

app = Flask(__name__)

changable = [0, 0]

@app.route('/')
def home():
  return json.dumps(changable)

@app.route('/change', methods=["POST"])
def change():
    data = request.get_json()
    alt = int(data.get("altitude", 404))
    azi = int(data.get("azimuth", 404))
    global changable
    changable = [alt, azi]
    return "ok", 200
