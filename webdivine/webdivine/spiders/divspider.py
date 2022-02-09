from gc import callbacks
import scrapy
from urllib.parse import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DivSpider(CrawlSpider):
    name = 'webdivine'
    
    def __init__(self, start=None, *args, **kwargs):
        self.start_domain = urlparse(start).netloc
        self.start_urls = [start]
        self.rules = (
            Rule(LinkExtractor(allow=self.start_domain), callback='parse_img', follow=True)  # https://www.geeksforgeeks.org/how-to-download-files-with-scrapy/
        )
        super(DivSpider, self).__init__(*args, **kwargs)  # https://stackoverflow.com/questions/39532119/scrapy-rules-set-inside-init-are-ignored-by-crawlspider


    def parse_img(self, response):
        image_package = scrapy.Item()
        # POPULATE image_urls ATTRIBUTE FOR image_package