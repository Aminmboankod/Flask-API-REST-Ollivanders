from src.domain.normalItem import NormalItem
from src.domain.item import Item

class Sulfuras(NormalItem):

    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    
    def updateQuality(self):
        assert self.quality == 80, "Calidad de %s distinta de 80" % self.__class__.__name__
        