from flask import Flask, jsonify, request
from pickle import load
#from tensorflow import keras
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Examen":"Santiago Collaguazo"})

@app.route('/',methods=['POST'])
def predecir():
    #if not request.json:
        #abort(400)
        
    array = "{"metar": [request.json['tempd_o'],request.json['rh_o'],request.json['dir_o'],request.json['spd_o'],request.json['mslp_o'],request.json['visibility_o'],request.json['skyc1_o'],request.json['skyc2_o'],
    request.json['skyc3_o'],request.json['wxcodes_o'],request.json['year'],request.json['month'],
    request.json['day'],request.json['hora'],request.json['minutos']]}"
    return jsonify({"Examen":"Santiago Collaguazo","Label":array})
    #data = json.loads(array)
    #dList = data['metar']
    #model = keras.models.load_model("model.h5")
    #scaler = load(open('scaler.pkl', 'rb'))
    #scaList=scaler.transform(dList)
    #predic=model.predict(scaList)
    #return jsonify({"Examen":"Santiago Collaguazo","Label":predic})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
