
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import gspread
import os
from scrapy.exceptions import DropItem

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class FilterEmptyField:
    def __init__(self):
        self.fields = ['keyword','asin','url','title','price','rating','thumbnail_url']
    def process_item(self,item,spider):
        for field in self.fields:
            if not item.get(field) or item.get(field) == "":
                spider.logger.warning(f"Missing {field} in item: {item}")
                raise DropItem(f"Missing {field} in item: {item}")
        return item

class AmazonPipeline:
    def open_spider(self, spider):
        cred_path = os.path.abspath("F:/python practice/amazon/amazon/cred.json")
        self.file_path = gspread.service_account(filename=os.path.join(os.getcwd(), cred_path))
        self.sheet = self.file_path.open("scrapetosheet").sheet1

    def process_item(self, item, spider):
        adp = ItemAdapter(item)
        self.sheet.append_row([
            adp.get('keyword', ''),
            adp.get('asin', ''),
            adp.get('url', ''),
            adp.get('title', ''),
            adp.get('price', ''),
            adp.get('rating', ''),
            adp.get('thumbnail_url', '')
        ])
        return item
