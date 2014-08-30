from scrapy.item import Item, Field


class SocrataItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = Field()
    url = Field()
    views = Field()
