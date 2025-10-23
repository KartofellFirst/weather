from flask import Flask, request, render_template
import json

app = Flask(__name__)

changable = [0, 0]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/update', methods=["GET"])
def give_data():
    return json.dumps({"alt": changable[0], "azi": changable[1]})

@app.route('/change', methods=["POST"])
def change():
    data = request.get_json()
    alt = int(data.get("altitude", 404))
    azi = int(data.get("azimuth", 404))
    global changable
    changable = [alt, azi]
    return "ok", 200
