from gc import callbacks
import scrapy
import items
from urllib.parse import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DivSpider(CrawlSpider):
    name = 'webdivine'
    
    def __init__(self, start=None, target_dom_element=None, *args, **kwargs):
        # self.start_domain = urlparse(start).netloc
        # self.start_urls = [start]
        # self.target_dom_element = target_dom_element

        # TEMP
        self.start_domain = 'en.wikipedia.org'
        self.start_urls = ['https://en.wikipedia.org/wiki/Main_Page']
        self.target_dom_element = "//div[@id='content']"


        self.rules = (
            Rule(LinkExtractor(allow=self.start_domain), callback='parse_image', follow=True)  # https://www.geeksforgeeks.org/how-to-download-files-with-scrapy/
        )
        super(DivSpider, self).__init__(*args, **kwargs)  # https://stackoverflow.com/questions/39532119/scrapy-rules-set-inside-init-are-ignored-by-crawlspider


    def parse_image(self, response):
        image_package = items.WebdivineImagePackage
        image_search_target = f'{self.target_dom_element}//img/src' if self.target_dom_element else '//img/src'  # e.g. //div[@id='content']//img[@src]
        image_package.image_urls = response.xpath(image_search_target).getall()
        return image_package
        