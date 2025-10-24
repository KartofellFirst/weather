from flask import Flask, request, render_template, send_from_directory
import json

app = Flask(__name__)

changable = [50, 236, 43, 25]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/update', methods=["GET"])
def give_data():
    return json.dumps({"alt": changable[0], "azi": changable[1], "hum": changable[2], "temp": changable[3]})

@app.route('/change', methods=["POST"])
def change():
    data = request.get_json()
    alt = int(data.get("altitude", 404))
    azi = int(data.get("azimuth", 404))
    hum = int(data.get("humidity", 404))
    temp = int(data.get("temperature", 404))
    global changable
    changable = [alt, azi, hum, temp]
    return "ok", 200
