import scrapy
from feedscraper.items import ReutersFeed

class ReutersSpider(scrapy.Spider):
    name = 'reuters'
    allowed_domains = ['www.reuters.com']
    start_urls = [
        'http://www.reuters.com/tools/rss',
    ]

    def parse(self, response):
        urls = set(response.css('.feedUrl::text').extract())
        return [ReutersFeed(url=url) for url in urls]
