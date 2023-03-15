

from src.domain.item import Item
from src.domain.interfaz import Updateable


class NormalItem(Item, Updateable):
    def __init__(self,  name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def getName(self):
        return self.name

    def getQuality(self):
        return self.quality

    def getSellIn(self):
        return self.sell_in

    def setSellIn(self):
        self.sell_in = self.sell_in + -1

    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality = self.quality + value

    def updateQuality(self):
        if self.getSellIn() > 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSellIn()  


        