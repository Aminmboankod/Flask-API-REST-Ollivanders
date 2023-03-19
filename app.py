from flask import Flask, jsonify

from src.repository.apiDB import inventario



app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a mi API"

@app.route('/inventario')
def get_items():
    items = inventario()
    return jsonify(items.json())

if __name__=="__main__":
    app.run(debug=True)
