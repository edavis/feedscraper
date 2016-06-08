import scrapy

class ReutersFeed(scrapy.Item):
    url = scrapy.Field()
