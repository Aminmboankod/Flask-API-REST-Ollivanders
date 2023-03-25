
from src.domain.normalItem import NormalItem
from src.domain.items.sulfuras import Sulfuras
from src.domain.items.agedBrie import AgedBrie
from src.domain.items.backstage import Backstage
from src.domain.items.conjured import Conjured

class Service():



    item_list = [
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