
from flask import Flask, jsonify


from src.repository.apiDB import delete, insert, inventory, item_db
from src.repository.updateDB import inventory_to_object
from src.services.services import Service

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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
    return "\n\n-----------Inventario actualizado------------\n\n"

@app.route('/actualizar/<name>')
def update_one(name):
    new_string = name.replace("+", " ")
    item = item_db(new_string)
    inventory_to_object(item)
    return f"\n\n----------{new_string} ha sido actualizado-----------\n\n"

@app.route('/filter/<name>')
def filter(name):
    new_string = name.replace("+", " ")
    return item_db(new_string)

@app.route('/reiniciar')
def reset():
    delete()
    for object in Service.item_list:
        item = { 'name': object.getName(), 'sell_in': object.getSellIn(), 'quality': object.getQuality() }
        insert(item)
    return "\n\n-------------Reinicio exitoso----------\n\n"

if __name__=="__main__":
    app.run(debug=True)
