from domain.normalItem       import NormalItem
from domain.items.agedBrie   import AgedBrie
from domain.items.backstage  import Backstage
from domain.items.conjured   import Conjured
from domain.items.sulfuras   import Sulfuras
from domain.gildedRose       import GildedRose


if __name__=="__main__":

    '''
        The intention is to create a database that supplies 
        the data stored in the "itemList" variable to do without it
    '''
    
    itemList = [
                NormalItem("+5 Dexterity Vest", 10, 20),
                AgedBrie("Aged Brie", 2, 0),
                NormalItem("Elixir of the Mongoose", 5, 7),
                Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 49),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49),
                Conjured("Conjured Mana Cake", 3, 6)
    ]

   
    inventory = GildedRose(itemList)

    for item in itemList:
        inventory.update_inventory()