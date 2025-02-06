from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazon.spiders.amazon_search import AmazonSearchSpider

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(AmazonSearchSpider)
    process.start()
