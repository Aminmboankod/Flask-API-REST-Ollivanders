from src.domain.item import Item
from src.domain.normalItem import NormalItem

class Backstage(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    
    def update_quality(self):

        if self.sell_in <= 10:
            self.setQuality(+2)
            
        elif self.sell_in <= 5:
            self.setQuality(+3)

        elif self.sell_in < 0:
            self.quality = 0
        else:
            self.setQuality(+1)

        self.setSellIn()