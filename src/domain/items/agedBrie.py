from src.domain.normalItem import NormalItem
from src.domain.item import Item


class AgedBrie(NormalItem):

    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)


        
    def updateQuality(self):
        if self.sellIn > 0:
            self.setQuality(+1)
        else:
            self.setQuality(+2)
        self.setSellIn()



        