
from flask import Flask, jsonify

from src.repository.apiDB import inventory, item_db
from src.repository.updateDB import inventory_to_object


app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a mi API"

@app.route('/inventario')
def get_items():
    items = inventory()
    return jsonify(items)

@app.route('/actualizar')
def update():
    items = inventory()
    inventory_to_object(items)
    return "-----------Inventario actualizado------------\n"

@app.route('/actualizar/<name>')
def update_one(name):
    new_string = name.replace("+", " ")
    item = item_db(new_string)
    inventory_to_object(item)
    return f"----------{new_string} ha sido actualizado-----------\n"

@app.route('/filter/<name>')
def filter(name):
    new_string = name.replace("+", " ")
    return item_db(new_string)



if __name__=="__main__":
    app.run(debug=True)
