# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WebdivinePipeline:
    def process_item(self, item, spider):
        print(item.images)
        return item

# Plan is to extend and override the ImagesPipeline, see these links for more info:
# https://docs.scrapy.org/en/latest/topics/media-pipeline.html#topics-media-pipeline-override
# https://docs.scrapy.org/en/latest/topics/media-pipeline.html
# Need to plan out exactly how I want images to be randomly selected/how I want storage space
# to be bounded...this will determine where I do that selection and bounding