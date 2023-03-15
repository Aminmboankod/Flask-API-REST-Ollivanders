class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.quality = quality 
        self.sell_in = sell_in
    
    
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
