import json
from flask import Flask, jsonify

from src.repository.apiDB import inventory
from src.repository.updateDB import inventory_to_object


app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a mi API"

@app.route('/inventario')
def get_items():
    response = inventory()
    response = json.loads(response.text)
    items = response.get('documents')
    return jsonify(items)

@app.route('/update')
def update():
    inventory_to_object(get_items())
    get_items()


if __name__=="__main__":
    app.run(debug=True)
