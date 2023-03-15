from src.domain.normalItem import NormalItem
from src.domain.item import Item
class Conjured(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSellIn()