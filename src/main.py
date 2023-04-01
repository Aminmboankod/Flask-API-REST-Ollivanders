from domain.gildedRose       import GildedRose
from services.services       import Service

if __name__=="__main__":

    itemList = Service.item_list

   
    inventory = GildedRose(itemList)

    for item in itemList:
        inventory.update_inventory()