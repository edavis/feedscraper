import scrapy

class ReutersFeed(scrapy.Item):
    url = scrapy.Field()

class Feed(scrapy.Item):
    url = scrapy.Field()
