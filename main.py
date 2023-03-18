from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    #load models("modelo.h5")
    #load_scaler("scaler.pkl")
    #X=scaler.transform(X)
    #predic=model.predict(X)[0]
    #return jsonify({predic})
    return jsonify({"Examen 3 /n Santiago Collaguazo"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
