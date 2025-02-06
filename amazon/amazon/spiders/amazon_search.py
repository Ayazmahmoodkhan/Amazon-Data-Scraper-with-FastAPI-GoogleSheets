import scrapy
from urllib.parse import urljoin
from amazon.items import AmazonItem

class AmazonSearchSpider(scrapy.Spider):
    name = "amazon_search"

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    def __init__(self, keyword=None, *args, **kwargs):
        super(AmazonSearchSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword

    def start_requests(self):
        if self.keyword:
            amazon_search_url = f'https://www.amazon.com/s?k={self.keyword}&page=1'
            yield scrapy.Request(url=amazon_search_url, callback=self.parse_search_results,
                                 meta={'keyword': self.keyword, 'page': 1})

    def parse_search_results(self, response):
        page = response.meta['page']
        keyword = response.meta['keyword']

        product_search = response.css("div.s-result-item[data-component-type=s-search-result]")
        if not product_search:
            self.log("No products found on this page")

        for product in product_search:
            relative_url = product.css("a::attr(href)").get()
            self.log(f"Extracted relative URL: {relative_url}")

            asin = None
            product_url = None

            if relative_url and '/dp/' in relative_url:
                asin = relative_url.split('/dp/')[1].split('/')[0]
                product_url = urljoin('https://www.amazon.com', relative_url).split("?")[0]
            else:
                continue

            amazonItem = AmazonItem()

            amazonItem["asin"] = asin
            amazonItem["keyword"] = keyword
            amazonItem["url"] = product_url
            amazonItem["title"] = product.css("a>h2>span::text").get()
            amazonItem["price"] = product.css(".a-price[data-a-size=xl] .a-offscreen::text").get()
            amazonItem["rating"] = product.xpath("//a/i/span/text()").get().split(" ")[0]
            amazonItem["thumbnail_url"] = product.css("img.s-image::attr(src)").get()
            yield amazonItem

        if page == 1:
            available_pages = response.xpath(
                '//*[contains(@class, "s-pagination-item")][not(has-class("s-pagination-separator"))]/text()'
            ).getall()


            last_page = available_pages[-1] if available_pages else 1
            for page_num in range(2, int(last_page) + 1):  
                amazon_search_url = f'https://www.amazon.com/s?k={keyword}&page={page_num}'
                yield scrapy.Request(url=amazon_search_url, callback=self.parse_search_results,
                                     meta={'keyword': keyword, 'page': page_num})
