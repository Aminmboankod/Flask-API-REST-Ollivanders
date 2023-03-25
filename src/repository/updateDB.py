from domain.normalItem import NormalItem
from domain.items.sulfuras import Sulfuras
from domain.items.agedBrie import AgedBrie
from domain.items.backstage import Backstage
from domain.items.conjured import Conjured
from repository.apiDB import update_db


def inventory_to_object(inventary):

    for item in inventary:
        update_item(item)

# función para actualizar el inventario
def update_item(object):

    # Creo un objeto y lo actualizo en función del nombre del item

    if "Aged Brie" in object["name"]:
        item = AgedBrie(object["name"], object["sell_in"], object["quality"])
        item.update_quality()

    elif "Backstage passes" in object["name"]:
        item = Backstage(object["name"], object["sell_in"], object["quality"])
        item.update_quality()

    elif "Conjured" in object["name"]:
        item = Conjured(object["name"], object["sell_in"], object["quality"])
        item.update_quality()

    elif "Sulfuras" in object["name"]:
        item = Sulfuras(object["name"], object["sell_in"], object["quality"])
        item.update_quality()

    else:
        item = NormalItem(object["name"], object["sell_in"], object["quality"])
        item.update_quality()

    return object_to_inventory(item)


def object_to_inventory(item):
    update_db(item)