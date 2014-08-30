from scrapy.item import Item, Field

class Web2PyItem(Item):
    text = Field()
    url = Field()
