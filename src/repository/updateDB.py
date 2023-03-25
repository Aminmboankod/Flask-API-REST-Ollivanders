from src.domain.normalItem import NormalItem
from src.domain.items.sulfuras import Sulfuras
from src.domain.items.agedBrie import AgedBrie
from src.domain.items.backstage import Backstage
from src.domain.items.conjured import Conjured
from src.repository.apiDB import delete_one, insert


def inventory_to_object(inventary):
    
    for item in inventary:
        post = update_item(item)
        delete_one(item)
        object_to_inventory(post)

# función para actualizar el inventario
def update_item(object):

    # Creo un objeto y lo actualizo en función del nombre del item

    if object["name"] == "Aged Brie":
        item = AgedBrie(object["name"], object["sell_in"], object["quality"])


    elif object["name"] == "Backstage passes to a TAFKAL80ETC concert":
        item = Backstage(object["name"], object["sell_in"], object["quality"])


    elif object["name"] == "Conjured Mana Cake":
        item = Conjured(object["name"], object["sell_in"], object["quality"])


    elif object["name"] == "Sulfuras, Hand of Ragnaros":
        item = Sulfuras(object["name"], object["sell_in"], object["quality"])


    else:
        item = NormalItem(object["name"], object["sell_in"], object["quality"])
        
        
    item.update_quality()

    item_inventory = { 'name': item.getName(), 'sell_in': item.getSellIn(), 'quality': item.getQuality() }
    return item_inventory


def object_to_inventory(item):
    insert(item)