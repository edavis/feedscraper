import scrapy
from feedscraper.items import Feed

class NYTimesSpider(scrapy.Spider):
    name = 'nytimes'
    allowed_domains = ['www.nytimes.com']
    start_urls = [
        'http://www.nytimes.com/services/xml/rss/index.html',
    ]

    def parse(self, response):
        urls = set()
        top = set(filter(lambda url: url != 'javascript:void(0);', response.css('.rssSection a::attr("href")').extract()))
        sub = set(response.css('.insetRSS a::attr("href")').extract())

        urls.update(top)
        urls.update(sub)
        return [Feed(url=url.strip()) for url in urls]
