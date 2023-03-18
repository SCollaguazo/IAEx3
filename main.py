from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"Examen"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
