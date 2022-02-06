import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DivSpider(CrawlSpider):
    name = 'webdivine'
    
    def __init__(self, start=None, *args, **kwargs):
        super(DivSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start]

    def parse(self, response):
        