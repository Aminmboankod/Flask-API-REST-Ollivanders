import json
from flask import Flask, jsonify

from src.repository.apiDB import inventario



app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a mi API"

@app.route('/inventario')
def get_items():
    response = inventario()
    response = json.loads(response.text)
    items = response.get('documents')
    return jsonify(items)

if __name__=="__main__":
    app.run(debug=True)
