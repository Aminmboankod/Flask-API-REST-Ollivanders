from src.domain.normalItem import NormalItem
from src.domain.item import Item


class AgedBrie(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)


        
    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(+1)
        else:
            self.setQuality(+2)
        self.setSellIn()



        